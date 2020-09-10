import pyttsx3
import datetime

engine=pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(Time)

time_()