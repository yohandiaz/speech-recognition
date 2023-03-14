import file_loader as fl
import pathlib

import speech_recognition as sr
engine = sr.Recognizer()

audio_file_path = str(pathlib.Path(__file__).parent.resolve()) + "/"
audio_file_path += input("Insert the name of the file: ")

audioToText(audio_file_path)

# read mp3 file
def audioToText(file_path):
    
    # Converts the audio file to wav format if it is not
    convertedFileName = fl.load_audio_file(file_path)

    with sr.AudioFile(convertedFileName) as source:
        print('Analyzing file...')
        audio = engine.record(source)

    # extract and print text

    text = engine.recognize_google(audio, language="es-ES")
    print(f'Text: {text}')
    txtFile = open('textRecognized.txt', 'a')
    txtFile.writelines(text)
