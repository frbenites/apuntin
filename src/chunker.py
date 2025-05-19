from pydub import AudioSegment
import os

def chunker(input_path, output_dir, chunk_length_min=7):
    '''
    This function takes an audio file and splits it into chunks of a certain length.
    :param input_path: Path to audio file we want to chunk
    :param output_dir: Directory where the chunks will be saved
    :param chunk_length_min: Length of each chunk in minutes
    '''
    audio = AudioSegment.from_file(input_path)
    chunk_length_ms = chunk_length_min * 60 * 1000

    os.makedirs(output_dir, exist_ok=True)
    chunk_paths = []

    for idx in range(0, len(audio), chunk_length_ms):
        chunk = audio[idx:idx + chunk_length_ms]
        chunk_name = os.path.join(output_dir, f"chunk_{len(chunk_paths)}.mp3")
        # Open the file yourself so export() uses this handle and closes it at block end
        with open(chunk_name, "wb") as f:
            chunk.export(f, format="mp3")
        chunk_paths.append(chunk_name)
        print(f"Created chunk: {chunk_name}")

    return chunk_paths