import win32com.client
import os
import speech_recognition as sr
import pyaudio
import webbrowser
from sitelist import sites
from ai import *



speaker = win32com.client.Dispatch('SAPI.SpVoice')

def say(tts):
     speaker.Speak(tts)

def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          r.pause_threshold = 0.6
          audio = r.listen(source)
          try:   
            query = r.recognize_google(audio, language="en-US")
            print(f"User said: {query}")
            return query
          except Exception as e:
            print("I couldn't understand you, please try again.")
            return "I couldn't understand you, please try again."

if __name__ == '__main__':
    liveChat = True
    print("Listening...")
    query = takeCommand()
    for site in sites:
      if f"Open {site[0]}".lower() in query.lower():
        say(f"Opening {site[0]}")
        webbrowser.open(site[1])
        takeCommand()
      elif "Ask AI".lower() in query.lower():
        response = askAI(query.lower())
        say(response)
        takeCommand()
      elif "Hi".lower() in query.lower():
        say("Hello Simmer, how are you today?")
        takeCommand()
      elif "Bye".lower() in query.lower():
        liveChat = False
        say('Goodbye!')