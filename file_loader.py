from pydub import AudioSegment

def load_audio_file(file_path):
    # Get the file extension from the file path
    file_extension = file_path.split(".")[-1]

    # List of supported audio file formats
    supported_formats = ["mp3", "mp4", "wav", "ogg"]

    # If the file format is not supported, convert it to MP3 using Pydub
    if file_extension not in supported_formats:
        # Create a new file path with a .mp3 extension
        mp3_path = file_path.rsplit(".", 1)[0] + ".mp3"
        # Load the audio data from the original file
        audio = AudioSegment.from_file(file_path, format=file_extension)
        # Export the audio data to the new MP3 file using Pydub
        audio.export(mp3_path, format="mp3")
        # Update the file path and extension to the new MP3 file
        file_path = mp3_path
        file_extension = "mp3"

    # Load the audio data from the file using Pydub
    return AudioSegment.from_file(file_path, format=file_extension)