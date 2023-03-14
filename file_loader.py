from pydub import AudioSegment
import os

def load_audio_file(file_path):
    # Get the file extension from the file path
    file_extension = file_path.split(".")[-1]

    # List of supported audio file formats
    supported_formats = ["mp3", "mp4", "wav", "ogg"]

    # If the file format is not supported, convert it to MP3 using Pydub
    if file_extension in supported_formats:
        return convert_to_wav(file_path)
    else:
        print("Format " + file_extension + "is not supported, used mp3 mp4 wav or ogg instead")

def convert_to_wav(file_path):
    """
    Convierte un archivo de audio a formato wav utilizando la biblioteca pydub.
    """
    # Carga el archivo de audio utilizando la biblioteca pydub.
    sound = AudioSegment.from_file(file_path)

    # Define el nombre del archivo de salida.
    wav_file = os.path.splitext(file_path)[0] + ".wav"

    # Exporta el archivo de audio como formato wav.
    sound.export(wav_file, format="wav")

    return wav_file

