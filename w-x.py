from faster_whisper import WhisperModel
from src.config import p, execution_device, torch
from src.logger import logger
import shutil, re, os, pysubs2
import whisperx
import gc, json

def test(temp_path):
    file_name = temp_path.split('/')[-1].split('.')[0]
    #wav_path = f"{temp_path.split('.')[0]}.wav"
    #audio = AudioSegment.from_file(temp_path, format="mp4")
    #audio = audio.normalize()
    #audio = audio.set_frame_rate(44100)
    #audio.export(wav_path, format="wav", parameters=["-acodec", "pcm_s24le"])

    #whisper_model_size = "large-v3"
    whisper_model_size = "distil-large-v3"
    STTModel = WhisperModel(whisper_model_size, device=execution_device)
    segments, _ = STTModel.transcribe(temp_path, beam_size=5, language="zh",initial_prompt="This task is to provided course transcripts.", condition_on_previous_text=False)
    results= []
    for s in segments:
        segment_dict = {'start':s.start,'end':s.end,'text':s.text}
        logger.debug(segment_dict)
        if len(results) > 0 and results[-1]['text'] == segment_dict['text']:
            continue
        results.append(segment_dict)
    subs = pysubs2.load_from_whisper(results)
    vtt_destination = object_key.replace('mp4', 'vtt')
    txt_destination = object_key.replace('mp4', 'txt')
    tmp_vtt_path = f"{p.DIR_UPLOAD}/{file_name}.vtt"
    tmp_txt_path = f"{p.DIR_UPLOAD}/{file_name}.txt"
    subs.save(tmp_vtt_path)

def test2(temp_path):
    execution_device = "cuda" if torch.cuda.is_available() else "cpu"
    compute_type = "float16" if execution_device=="cuda" else "int8"
    print(f"Device name:: {execution_device}, Compute type::{compute_type} .")
    HF_TOKEN = "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"
    STTModel = whisperx.load_model("large-v2", execution_device, compute_type=compute_type)
    audio = whisperx.load_audio(temp_path)
    before_alignment = STTModel.transcribe(audio, batch_size=16, language="zh")
    gc.collect()
    model_a, metadata = whisperx.load_align_model(language_code=before_alignment.get("language"), device=execution_device)
    after_alignment = whisperx.align(before_alignment.get("segments"), model_a, metadata, audio, execution_device, return_char_alignments=False)
    diarize_model = whisperx.DiarizationPipeline(use_auth_token=HF_TOKEN, device=execution_device)
    diarize_segments = diarize_model(audio, min_speakers=1, max_speakers=3)
    speakers_alignment = whisperx.assign_word_speakers(diarize_segments, after_alignment)
    return speakers_alignment

def tovtt(path):
    with open(path, 'r', encoding='utf-8') as f:
        results = json.load(f)
    print(results)
    subs = pysubs2.load_from_whisper(results)
    subs.save(f"./data/data.vtt")

if __name__ == '__main__':
    object_key= f"667ac9e1ffce39e72163ace0/9f47dcb5944d7ef30dd9a39edfbdb0cc_c6011d8eebc64d60b667abd930cfb298_0.mp4"
    #temp_path = f"{p.DIR_DOWNLOAD}/{object_key}"
    #test2(temp_path)
    tovtt(f"./data/data.json")
    
    
    
    
async def monitor_sqs_deletions():
    queue_url = 'https://sqs.ap-northeast-1.amazonaws.com/661990540174/oneboard_mp4_created_event_queue'
    logger.info(f"開始監聽 SQS 隊列: {queue_url[30:]}")
    sqs_client = boto3.client('sqs', region_name=p.AWS_REGION ,aws_access_key_id=p.AWS_ACCESS_KEY_ID, aws_secret_access_key=p.AWS_SECRET_ACCESS_KEY)
    previous_count = 0
    while True:
        try:
            # 獲取隊列屬性
            response = sqs_client.get_queue_attributes(
                QueueUrl=queue_url,
                AttributeNames=['All']
            )
            print(response)
            # 計算當前消息總數
            current_count = int(response['Attributes']['ApproximateNumberOfMessages']) + \
                            int(response['Attributes']['ApproximateNumberOfMessagesNotVisible'])
            
            # 檢查是否有消息被刪除
            if current_count < previous_count:
                deleted_count = previous_count - current_count
                print(f"{datetime.now()}: 檢測到 {deleted_count} 條消息被刪除")
            
            previous_count = current_count
            print(previous_count, current_count)
            # 等待一段時間再次檢查
            time.sleep(10)  # 每10秒檢查一次，可以根據需要調整
        except Exception as e:
            print(f"發生錯誤: {e}")
            time.sleep(30)  # 發生錯誤時，等待30秒後重試
            
            


"""
#segments, _ = SpeechRecognitionModel.transcribe(temp_path, beam_size=5, language="zh",initial_prompt="This task is to provided course transcripts.")
        #results= []
        #for s in segments:
        #    segment_dict = {'start':s.start,'end':s.end,'text':s.text}
        #    if len(results) > 0 and results[-1]['text'] == segment_dict['text']:
        #        continue
        #    logger.debug(segment_dict)
        #    results.append(segment_dict)
"""