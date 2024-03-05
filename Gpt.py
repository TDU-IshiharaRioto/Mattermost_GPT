from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "You are a chatbot"
        },
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(completion.choices[0].message)