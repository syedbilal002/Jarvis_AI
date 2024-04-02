import speech_recognition as sr #pip install speechrecognition

# 1 - Listen : Hindi or English

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,4) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")

    except:
        return ""
    
    query = str(query).lower()
    return query

# 2 - Translation



# 3 - Connect

def Mic():
    query = Listen()
    #data = TranslationHinToEng(query)
    data = query
    print(f"You : {data}.")
    return data

