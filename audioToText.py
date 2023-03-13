import file_loader as fl

import speech_recognition as sr
engine = sr.Recognizer()

# read mp3 file

mp3FileName = fl.load_audio_file("test.mp3")

