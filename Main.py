import speech_recognition as sr
import wikipedia
import pyaudio
import openai
import os
import pyttsx3
import webbrowser
import datetime
import random
import numpy as np
from Config import apikey

chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Bilal: {query}\n Belvin: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Belvin"

if __name__ == "__main__":
    print('PyCharm')
    say("Belvin A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"],["instagram", "https://www.instagram.com"], ["facebook", "https://www.facebook.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
                # todo: Add a feature to play a specific song
                if "open music" in query:
                    musicPath = "C:/Users/MCC COMPUTERS/Downloads/beautiful music.mp3"
                    os.system(f"open {musicPath}")

                elif "the time" in query:
                    hour = datetime.datetime.now().strftime("%H")
                    min = datetime.datetime.now().strftime("%M")
                    say(f"Sir the time is {hour} past {min} minutes")

                elif "open Camera".lower() in query.lower():
                    os.system(f"open /System/Applications/Camera.app")

                elif "open PyCharm".lower() in query.lower():
                    os.system(f"open C:\Program Files\JetBrains\PyCharm Community Edition 2024.3.2\bin\pycharm64.exe")

                elif "open Visual Studio Code".lower() in query.lower():
                    os.system(f"open C:\ Users\MCC COMPUTERS\AppData\Local\Programs\Microsoft VS Code\Code.exe")

                elif "open pass".lower() in query.lower():
                    os.system(f"open /Applications/Passky.app")

                elif "Using artificial intelligence".lower() in query.lower():
                    ai(prompt=query)

                elif "Jarvis Quit".lower() in query.lower():
                    exit()

                elif "reset chat".lower() in query.lower():
                    chatStr = ""

                else:
                    print("Chatting...")
                    chat(query)

        #say(query)
