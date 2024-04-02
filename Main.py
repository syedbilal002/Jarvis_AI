from Reply import ReplyIt
from ListenJarvis import Mic

import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

anss = int(input("Change Api Key :- \nPress 1 for Yes \nPress 2 for No \n"))
if anss==1:
    api = input("Enter the Api Key : ")
    file1 = open("Api.txt", "w")
    file1.write(api)
    file1.close()
else:
    
    print("Starting Jarvis, Please wait for a few seconds...")

    def MAIN():
        speak("Hello, Bro")
        while True:
            Data = Mic()
            Data = str(Data)

            if len(Data) < 3:
                pass

            else:
                Reply = ReplyIt(Data)
                print("AI  : ",Reply)
                speak(Reply)

    MAIN()



