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

def format_transcript(raw_transcript, title):
    """
    Formats raw transcript into well-structured markdown using ChatGPT
    """
    logger.info("🎨 Formatting transcript with ChatGPT...")
    
    system_prompt = """
You are “Apuntín”, an academic note‑taker.

### Hard rules  (the model **must** follow them)

1. **NO INVENTION** – do not add facts, examples or arguments that are absent from the transcript.
2. **Length cap** – output ≤ 1.2 × the number of words in the input chunk.  
   *If the transcript has ≤ 40 words, output a single, concise bullet or direct quote.*
3. Preserve the transcript’s meaning, but you may:
   • correct grammar  
   • remove fillers  
   • break long sentences.
4. Headings only when the chunk > 80 words.  
   *Otherwise skip headings and key‑takeaways sections.*
5. When you do use headings:  
   • H2 for main themes, H3 for sub‑themes.  
   • Bullet points start with “- ”.  
   • Definitions → `> **Definition**:`, formulas → `$$ … $$`, code → fenced blocks.
6. Return **pure Markdown** ⎯ no YAML front‑matter, no extra commentary.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": raw_transcript}
            ],
            max_tokens=4000,
            temperature=0.3
        )
        
        formatted_transcript = response.choices[0].message.content
        logger.info("✅ Transcript formatting complete.")
        return formatted_transcript
        
    except Exception as e:
        logger.error(f"❌ Error formatting transcript: {e}")
        logger.info("📝 Falling back to raw transcript with basic formatting...")
        # Fallback to basic formatting if ChatGPT fails
        return f"# {title}\n\n{raw_transcript}"
