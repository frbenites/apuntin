import whisper
import logging

logger = logging.getLogger(__name__)

def transcriptor(chunks_path, model_size="base"):
    """
    Transcribes audio chunks using AI    
    """
    model = whisper.load_model(model_size)
    transcripts = []

    logger.info("Loaded Whisper model:{model_size}")

    for path in chunks_path:
        logger.info(f"Transcribing chunk: {path}")
        try:
            result = model.transcribe(path, language="es")
            transcripts.append(result["text"])
        except Exception as e:
            logger.error(f"Got an error transcribing {path}: {e}")
    
    full_transcript = "\n".join(transcripts)
    logger.info("✅ Transcription complete.")
    return full_transcript
