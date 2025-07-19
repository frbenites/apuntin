import sys
import os

sys.path.append(os.getcwd())

from src.transcriptor import transcriptor

def test_transcription():
    test_audio_path = "tests/tests_jfk.flac"
    chunk_paths = [test_audio_path]

    full_transcript = transcriptor(chunk_paths)
    assert isinstance(full_transcript, str)

    with open("transcripts/test_transcript.md", "w") as f:
        f.write(f"# Test Transcript\n\n")
        f.write(full_transcript)
    assert os.path.exists("transcripts/test_transcript.md")

if __name__ == "__main__":
    test_transcription()