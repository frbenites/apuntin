import logging
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

logger = logging.getLogger(__name__)

def transcriptor(chunks_path):
    """
    Transcribes audio chunks using AI    
    """
    transcripts = []
    logger.info("Loaded Whisper model:{model_size}")

    for path in chunks_path:
        try:
            logger.info(f"Transcribing chunk: {path}")
            with open(path, "rb") as audio_file:
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            transcripts.append(response.text)
        except Exception as e:
            logger.error(f"Got an error transcribing {path}: {e}")
    
    full_transcript = "\n".join(transcripts)
    logger.info("✅ Transcription complete.")
    return full_transcript
