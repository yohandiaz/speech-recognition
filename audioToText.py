import file_loader as fl
import pathlib

import speech_recognition as sr
engine = sr.Recognizer()

# read mp3 file

audio_file_path = pathlib.Path(__file__).parent.resolve()
audio_file_path += input("Insert the name of the file: ")
convertedFileName = fl.load_audio_file(audio_file_path)

with sr.AudioFile(convertedFileName) as source:
    print('Analyzing file...')
    audio = engine.record(source)

# extract and print text

text = engine.recognize_google(audio, language="es-ES")
print(f'Text: {text}')
txtFile = open('textRecognized.txt', 'a')
txtFile.writelines(text)
