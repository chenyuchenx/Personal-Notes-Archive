from app.src.database import MongoDB
from .schema import *
from app.logger import logger
from app.config import p, s3
from datetime import datetime, timedelta
from langchain_community.callbacks import get_openai_callback
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from google.cloud import speech
import re, json, boto3

async def download_audio_from_url(url):
    parts = url.split('/')
    course_id = parts[3]
    record_id = parts[4].split('.')[0]
    bucket_name = "oneclass-record"
    prefix = f"{course_id}/"
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    logger.debug(f"download_audio_from_url:: {course_id}...{record_id}")
    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            if key.endswith(f'{record_id}.vtt'):
                logger.debug(f'Found .vtt file: {key}')
                s3.download_file(bucket_name, key, f"{p.DIR_TMP}/{course_id}.vtt")
                return True, f"{p.DIR_TMP}/{course_id}.vtt", f"{course_id}.vtt"
    else:
        pass
    return False, "", ""

async def time_to_seconds(time_str):
    """Convert time string (HH:MM:SS.mmm) to seconds."""
    hours, minutes, seconds = time_str.split(':')
    seconds, milliseconds = seconds.split('.')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000

async def seconds_to_time(seconds):
    """Convert seconds to time string (HH:MM:SS.mmm)."""
    return str(timedelta(seconds=seconds))

async def recognize_from_vtt_file(vtt_file_path, eventId, start_time="00:20:00.00"):

    start_time_seconds = await time_to_seconds(start_time)
    segment_duration_seconds = 30
    segments = []

    with open(vtt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    content = []
    current_time = None
    current_segment_start = start_time_seconds

    for line in lines:
        line = line.strip()
        if re.match(r'\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}', line):
            current_time = line.split(' --> ')[0]
            current_time_seconds = await time_to_seconds(current_time)
            if current_time_seconds >= current_segment_start + segment_duration_seconds:
                segments.append({
                    "text": ' '.join(content).strip(),
                    "start": await seconds_to_time(current_segment_start),
                    "end": await seconds_to_time(current_segment_start + segment_duration_seconds)
                })
                content = []
                current_segment_start += segment_duration_seconds
        elif current_time and await time_to_seconds(current_time) >= start_time_seconds:
            if not line.isdigit() and line:
                content.append(line)

    if content:
        segments.append({
            "text": ' '.join(content).strip(),
            "start": await seconds_to_time(current_segment_start),
            "end": await seconds_to_time(current_segment_start + segment_duration_seconds)
        })

    speech_text = json.dumps(segments, ensure_ascii=False, indent=4)
    speech_text_list = json.loads(speech_text)

    info = {"originals":speech_text_list}

    MongoDB.upsert_one(p.MONGODB_COLL_B_ANALYSIS, {'eventId':eventId}, {"$set": info})

    return speech_text_list

async def google_stt_form_uri(gcs_uri, eventId):
    gcp_speech_client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        language_code="zh-TW",
    )
    operation = gcp_speech_client.long_running_recognize(config=config, audio=audio)
    logger.debug(f"Waiting to complete... {gcs_uri}")
    response = operation.result(timeout=4800)
    start_time = timedelta(seconds=0, microseconds=0)
    segments = []
    for result in response.results:
        end_time = result.result_end_time
        segment_dict = {'start': str(start_time), 'end': str(end_time), 'text': result.alternatives[0].transcript}
        logger.info(f"Recognized::: {segment_dict}")
        segments.append(segment_dict)
        start_time = end_time
    
    info = {
        "situational_1":False,
        "situational_2":False,
        "situational_3":False,
        "originals":segments
    }

    MongoDB.upsert_one(p.MONGODB_COLL_B_ANALYSIS, {'eventId':eventId}, {"$set": info})

    return segments

async def business_audio_check_situational_1(data, eventId):
    speech_text_list = '\n'.join(f"{entry['start']}: {entry['text'].strip()}"for entry in data)
    s1_list = MongoDB.get_many(p.MONGODB_COLL_B_SITUATIONAL_1, [{"$project": {"_id": 0}}])
    parser = JsonOutputParser(pydantic_object=CheckAudio)
    ruleLst = "\n".join([f"{item['itemNumber']}. {item['desc']}" for item in s1_list])
    prompt = PromptTemplate(
        template="""
        # 檢查語音原始內容中是否違反出現如下相似處，並且符合程度需達到95%才截取：
        ## 規則:
        {rule}
        ## 語音原始內容（業務與家長的對話）:
        {content}
        ## 輸出格式:
        {format_instructions}
        """,
        input_variables=["content"],
        partial_variables={"format_instructions": parser.get_format_instructions(), "rule":ruleLst},
    )
    chain = prompt | p.chatllm | parser
    with get_openai_callback() as cb:
        response = await chain.ainvoke(input={"content":speech_text_list})
    logger.debug(f"Total Cost: {cb.total_cost}, Total Tokens: {cb.total_tokens}")
    MongoDB.upsert_one(p.MONGODB_COLL_B_ANALYSIS, {'eventId':eventId}, {"$set": {"situational_1": response}})
    return response

async def business_audio_check_situational_2(data, eventId):

    speech_text_list = '\n'.join(f"{entry['start']}: {entry['text'].strip()}"for entry in data)
    ruleData = MongoDB.get_many(p.MONGODB_COLL_B_SITUATIONAL_2, [{"$project": {"_id": 0}}, {"$sort": {"itemNumber": 1}}])
    rule = "\n".join([f"{item['itemNumber']}. {item['question']}" for item in ruleData])

    parser = JsonOutputParser(pydantic_object=ChekItemS2)
    prompt = PromptTemplate(
        template="""
        # 檢查以下問句是否出現在語音原始內容中，並且符合程度需達到98%才列出：
        ## 情境問句:
        {rule}
        ## 語音原始內容（業務與家長的對話）:
        {content}
        ## 輸出格式:
        {format_instructions}
        ## 注意如果語音原始內容不符合則輸出空陣列
        """,
        input_variables=["content"],
        partial_variables={"format_instructions": parser.get_format_instructions(), "rule":rule},
    )   
    chain = prompt | p.chatllm | parser
    with get_openai_callback() as cb:
        response = await chain.ainvoke(input={"content":speech_text_list})
    logger.debug(f"Total Cost: {cb.total_cost}, Total Tokens: {cb.total_tokens}, Check: {response}")
    checkItem = response.get("checkItem")
    if len(checkItem) == 0:
        MongoDB.upsert_one(p.MONGODB_COLL_B_ANALYSIS, {'eventId':eventId}, {"$set": {"situational_2": {"isViolation" : False,"data":[]}}})
        return []
    
    speech_text_list = '\n'.join(f"{entry['start']} -> {entry['end']} : {entry['text'].strip()}"for entry in data)
    ruleData = MongoDB.get_many(p.MONGODB_COLL_B_SITUATIONAL_2, [
        {"$match": {'itemNumber': {'$in': checkItem}}},
        {"$project": {"_id": 0}}
    ])
    ruleLst = "\n".join([f"問句{obj['itemNumber']}. {obj['question']} \n標準答案：{obj['answer']}" for obj in ruleData])
    parser = JsonOutputParser(pydantic_object=CheckAudio2)
    prompt = PromptTemplate(
        template="""
        # 檢查以下問句出現在語音原始內容中時,內容是否有遵守標準答案回答：
        ## 情境
        {rule}
        ## 語音原始內容（業務與家長的對話）:
        {content}
        ## 輸出格式：
        {format_instructions}
        ## 注意: 請找出所有不符合標準回答的項目並標記isViolation為false
        """,
        input_variables=["content"],
        partial_variables={"format_instructions": parser.get_format_instructions(), "rule":ruleLst}
    )   
    chain = prompt | p.chatllm | parser
    with get_openai_callback() as cb:
        response = await chain.ainvoke(input={"content":speech_text_list})
    response['data'] = [entry for entry in response['data'] if entry['start'] is not None]
    logger.debug(f"Total Cost: {cb.total_cost}, Total Tokens: {cb.total_tokens}, Res: {response}")
    MongoDB.upsert_one(p.MONGODB_COLL_B_ANALYSIS, {'eventId':eventId}, {"$set": {"situational_2": response}})
    return response

async def business_audio_check_situational_3(data, eventId):

    speech_text_list = '\n'.join(f"{entry['start']}: {entry['text'].strip()}"for entry in data)
    parser = JsonOutputParser(pydantic_object=CheckAudio3)
    text = s3_announcement()
    prompt = PromptTemplate(
        template="""
        # 檢查是否有成交宣告的意圖, 如果有此意圖根據給定的標準評估以下內容：
        ## 成交宣告規範:
        {announcement}
        ## 語音原始內容:
        {content}
        ## 輸出格式:
        {format_instructions}
        ## 注意：檢查對話與順序是否和"成交宣告規範"吻合(除了商品規格、付款資訊、會員資訊會有所不同之外, 其餘內容皆需與規範完全吻合)
        """,
        input_variables=["content"],
        partial_variables={"format_instructions": parser.get_format_instructions(), "announcement": text},
    )   
    chain = prompt | p.chatllm | parser
    with get_openai_callback() as cb:
        response = await chain.ainvoke(input={"content":speech_text_list})
    logger.debug(f"Total Cost: {cb.total_cost}, Total Tokens: {cb.total_tokens}, Check: {response}")
    MongoDB.upsert_one(p.MONGODB_COLL_B_ANALYSIS, {'eventId':eventId}, {"$set": {"situational_3": response}})
    return response

    