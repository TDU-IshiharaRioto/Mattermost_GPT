from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(
    organization=os.environ["OPENAI_ORGANIZATION"]
)
OpenAI.api_key = os.environ["OPENAI_API_KEY"]

@app.get("/greet")
def greet():
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "こんにちは"
            }
        ]
    )
    return {"message": completion.choices[0].message["content"]}

if __name__ == '__main__':
    print(greet())