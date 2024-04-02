# Open AI
fileopen = open("Api.txt","r")
API = fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv


openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyIt(question,chat_log = None):
        
    prompt = f'{chat_log}You : {question}\nJarvis : '
    response = completion.create(
        model = "text-davinci-003",
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    return answer
    