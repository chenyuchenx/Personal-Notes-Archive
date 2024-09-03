from faster_whisper import WhisperModel
from src.config import p, execution_device, whisper_model_size
from src.logger import logger
import shutil, re, os, pysubs2
import whisperx
import gc, json, numpy as np

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

import json, re
from typing import List, Dict

def parse_speech_segments(data: Dict) -> List[Dict]:
    segments = []
    current_segment = None

    for word in data['segments'][0]['words']:
        if current_segment is None or word['speaker'] != current_segment['speaker']:
            if current_segment:
                segments.append(current_segment)
            current_segment = {
                'start': word['start'],
                'end': word['end'],
                'speaker': word['speaker'],
                'text': word['word']
            }
        else:
            current_segment['end'] = word['end']
            if re.match(r'[A-Za-z0-9]', word['word']) and re.match(r'[A-Za-z0-9]', current_segment['text'][-1]):
                current_segment['text'] += ' '
            current_segment['text'] += word['word']

    if current_segment:
        segments.append(current_segment)

    return segments

def audio_trans_vtt(temp_path):
    compute_type = "float16" if execution_device=="cuda" else "int8"
    print(f"Device name:: {execution_device}, Compute type::{compute_type} .")
    STTModel = whisperx.load_model(whisper_model_size, execution_device, compute_type=compute_type)
    audio = whisperx.load_audio(temp_path)
    samples_per_5min = 5 * 60 * 16000
    num_splits = -(-len(audio) // samples_per_5min)
    parts = np.array_split(audio, num_splits)
    transcriptions = []
    total_duration = 0
    for i, part in enumerate(parts):
        print(f"Processing part {i+1}/{len(parts)}")
        result = STTModel.transcribe(part, batch_size=8, language="zh")
        for segment in result['segments']:
            segment['start'] += total_duration
            segment['end'] += total_duration
        transcriptions.extend(result['segments'])
        total_duration += len(part) / 1000
    # Speacker split
    model_a, metadata = whisperx.load_align_model(language_code="zh", device=execution_device)
    after_alignment = whisperx.align(transcriptions, model_a, metadata, audio, execution_device, return_char_alignments=False)
    diarize_model = whisperx.DiarizationPipeline(use_auth_token="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", device=execution_device)
    diarize_segments = diarize_model(audio, min_speakers=1, max_speakers=3)
    speakers_alignment = whisperx.assign_word_speakers(diarize_segments, after_alignment)
    segments = parse_speech_segments(speakers_alignment)
    return transcriptions, segments

def tovtt(path):
    with open(path, 'r', encoding='utf-8') as f:
        results = json.load(f)
    print(results)
    subs = pysubs2.load_from_whisper(results)
    subs.save(f"./data/data.vtt")


if __name__ == '__main__':
    object_key= f"667ac9e1ffce39e72163ace0/9f47dcb5944d7ef30dd9a39edfbdb0cc_c6011d8eebc64d60b667abd930cfb298_0.mp4"
    #temp_path = f"{p.DIR_DOWNLOAD}/{object_key}"
    #audio_trans_vtt(temp_path)
    tovtt(f"./data/before_alignment.json")