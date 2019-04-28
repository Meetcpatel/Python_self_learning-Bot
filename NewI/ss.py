import speech_recognition as sr

r = sr.Recognizer()

#mic = sr.Microphone()
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("You said", text)
except:
    print("Fails try again")
