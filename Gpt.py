from openai import OpenAI

clien = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a chatbot"
        },
        {
            "role": "user",
            "content": "こんにちは"
        }
    ]
)

print(completion.choices[0].message)