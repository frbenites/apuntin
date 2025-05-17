import unittest
import os
from pydub.generators import Sine
from src.chunk_audio import chunk_audio

class TestChunkAudio(unittest.TestCase):
    def setUp(self):
        """Prepare test audio and output directory."""
        self.test_audio_path = "audio/test_tone.mp3"
        self.output_dir = "chunks_test"

        # Generate a 3-minute sine wave tone (440Hz)
        duration_ms = 3 * 60 * 1000  # 3 minutes in milliseconds
        tone = Sine(440).to_audio_segment(duration=duration_ms)
        os.makedirs("audio", exist_ok=True)
        with open(self.test_audio_path, "wb") as f:
            tone.export(f, format="mp3")

    def test_chunk_audio(self):
        """Test that the audio is split into expected chunks."""
        chunk_length_min = 1
        chunks = chunk_audio(self.test_audio_path, self.output_dir, chunk_length_min)

        expected_chunks = 3  # 3 minutes total, 1-minute chunks
        self.assertEqual(len(chunks), expected_chunks)
        for chunk_path in chunks:
            self.assertTrue(os.path.exists(chunk_path))

    def tearDown(self):
        """Clean up all test files."""
        if os.path.exists(self.test_audio_path):
            os.remove(self.test_audio_path)

        if os.path.exists(self.output_dir):
            for f in os.listdir(self.output_dir):
                os.remove(os.path.join(self.output_dir, f))
            os.rmdir(self.output_dir)

if __name__ == "__main__":
    unittest.main()
