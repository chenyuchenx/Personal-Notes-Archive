from app.src.tools import *
from app.src.database import MongoDB
from app.logger import logger
from app.config import p
from urllib.parse import urlparse, parse_qs
import requests, tempfile, os

# ["sip-trial-course-record", "sip-call-recorded"]
async def consultant_invitation_voice_quality_inspection(evectDict):
    try:
        eventType = evectDict.get("eventType")
        eventId = evectDict.get("eventId")
        reqUrl = evectDict.get("url")
        evectDict = {key: evectDict[key] for key in evectDict if key not in ["url", "isProcess"]}
        logger.info(f"mongo save... {evectDict}")
        MongoDB.upsert_one(p.MONGODB_COLL_B_ANALYSIS, {'eventId':eventId}, {"$set": evectDict})

        if eventType == "sip-call-recorded":
            parsed_url = urlparse(reqUrl)
            bucket_name = parsed_url.path.split('/')[1]
            gcs_file_name = '/'.join(parsed_url.path.split('/')[2:])
            gcs_uri = f"gs://{bucket_name}/{gcs_file_name}"
            speech_text_list = await google_stt_form_uri(gcs_uri, eventId)

        elif eventType == "sip-trial-course-record":
            if reqUrl is None:
                 MongoDB.delete_one(p.MONGODB_COLL_KAFKA, {'eventId':eventId})
                 return
            have_file, temp_path, file_name = await download_audio_from_url(reqUrl)
            if have_file == False:
                 MongoDB.upsert_one(p.MONGODB_COLL_KAFKA, {'eventId':eventId}, {"$set": {"isProcess":"Error"}})
                 return
            speech_text_list = await recognize_from_vtt_file(temp_path, eventId, "00:20:00.00")
            os.remove(temp_path)
            logger.info(f"Temporary file {temp_path} deleted.")

        response = await business_audio_check_situational_1(speech_text_list, eventId)
        response = await business_audio_check_situational_2(speech_text_list, eventId)
        response = await business_audio_check_situational_3(speech_text_list, eventId)
        MongoDB.upsert_one(p.MONGODB_COLL_KAFKA, {'eventId':eventId}, {"$set": {"isProcess":True}})
    except Exception as e:
        logger.error(f"Error in consultant_invitation_voice_quality_inspection: {e}")
        MongoDB.delete_one(p.MONGODB_COLL_B_ANALYSIS, {'eventId':eventId})
        MongoDB.upsert_one(p.MONGODB_COLL_KAFKA, {'eventId':eventId}, {"$set": {"isProcess":"Error"}})