import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes
import os

#initialise the engine to convert text to audio
engine = pyttsx3.init()
#function to call os to open programs on command :D
def open_app(app_name):
    if "clock" in app_name:
        os.system("start ms-clock:")  
    elif "notepad" in app_name:
        os.system("start notepad")
    elif "calculator" in app_name:
        os.system("start calc")
    else:
        speak("Sorry, I don't know that app.")
#function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()
#change voice to female assistant
def set_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

# Record using sounddevice
def record_audio(duration=3, fs=44100):
    print("Listening...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Done Listening.")
    return np.squeeze(audio)

# Convert recorded audio to text
def listen():
    recognizer = sr.Recognizer()
    audio_data = record_audio()
    audio_bytes = audio_data.tobytes()

    audio = sr.AudioData(audio_bytes, sample_rate=44100, sample_width=2)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print(" Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Could not connect to recognition service.")
        return ""

# Voice assistant logic
def run_assistant():
    speak("Hey there! What can I do for you?")
    command = listen()

    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)
    elif "open" in command:
        open_app(command)
    elif "your name" in command:
        speak("I’m a voice assistant made in two minutes.")

    elif command.strip() == "":
        speak("I couldn't catch that. Try again.")

    else:
        speak("Sorry, I don't know that one. Try asking something else")

# main
set_voice()
run_assistant()
