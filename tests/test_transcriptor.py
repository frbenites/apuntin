import sys
import os

sys.path.append(os.getcwd())

from src.transcriptor import transcriptor, format_transcript

def test_transcription():
    test_audio_path = "tests/tests_jfk.flac"
    chunk_paths = [test_audio_path]

    # Test basic transcription
    full_transcript = transcriptor(chunk_paths)
    assert isinstance(full_transcript, str)

    # Test formatting
    formatted_transcript = format_transcript(full_transcript, "test_jfk")
    assert isinstance(formatted_transcript, str)
    assert len(formatted_transcript) > len(full_transcript)  # Should be longer due to formatting

    # Save formatted transcript
    with open("transcripts/test_transcript.md", "w", encoding="utf-8") as f:
        f.write(formatted_transcript)
    assert os.path.exists("transcripts/test_transcript.md")

if __name__ == "__main__":
    test_transcription()