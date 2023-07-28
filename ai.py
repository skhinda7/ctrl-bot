import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

def askAI(input):
    response = openai.ChatCompletion.create (
        model="gpt-3.5-turbo",
        max_tokens=256,
        messages= [
            {
                "role": "user", "content": input
            }
        ]
    )
    res = response.choices[0].message.content
    print(res)
    return res