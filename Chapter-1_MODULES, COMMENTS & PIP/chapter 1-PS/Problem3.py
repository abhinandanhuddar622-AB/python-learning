#   3). install external module and use to perform an operation of your interest(vaice output)
#        pip install pyttsx3

import pyttsx3    #pyttsx3 is a Text-to-Speech (TTS) library in Python.

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # Try 0 or 1 if you want male voice use 0, for female voice use 1

engine.say("hi Abhinandan, i am text to speech engine") #text to speech
engine.runAndWait()  #run  engine