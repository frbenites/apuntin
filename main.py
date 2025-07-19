import os
import sys
import shutil
import logging
import argparse
from src.chunker import chunker
from src.transcriptor import transcriptor

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def main(audio_path: str, chunk_length: int, keep_chunks: bool):
    if not os.path.exists(audio_path):
        logger.error(f"❌ File not found: {audio_path}")
        sys.exit(1)

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    chunks_dir = os.path.join("chunks", base_name)
    os.makedirs("transcripts", exist_ok=True)

    logger.info("🔪 Chunking audio...")
    chunk_paths = chunker(audio_path, chunks_dir, chunk_length_min=chunk_length)

    logger.info("🧠 Transcribing chunks...")
    transcript = transcriptor(chunk_paths)

    transcript_path = os.path.join("transcripts", f"{base_name}.md")
    with open(transcript_path, "w") as f:
        f.write(f"# Transcript: {base_name}\n\n")
        f.write(transcript)

    logger.info(f"✅ Transcript saved to {transcript_path}")

    if not keep_chunks:
        shutil.rmtree(chunks_dir)
        logger.info(f"🧹 Deleted temporary chunks in {chunks_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="🤖📝Apuntín - Desgrabar clases de la facu."
    )
    parser.add_argument("audio_path", help="Path to the audio file (mp3, flac, etc.)")
    parser.add_argument("--chunk-length", type=int, default=7, help="Chunk length in minutes (default: 7)")
    parser.add_argument("--keep-chunks", action="store_true", help="Keep audio chunks after transcription")

    args = parser.parse_args()
    main(args.audio_path, args.chunk_length, args.keep_chunks)
