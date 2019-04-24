import speech_recognition as sr
import sys

r=sr.Recognizer()
filename=sys.argv[1]
with sr.AudioFile(filename) as source:
    audio=r.listen(source)
try:
    print('System predicts:'+r.recognize_google(audio))
except Exception:
    print('Something went wrong')
