from openai import OpenAI
import os

OpenAI.api_key = os.environ["OPENAI_API_KEY"]
ai = OpenAI()

completion = ai.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a chatbot"
        }
    ]
)
print (completion.choices[0].message)