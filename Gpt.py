from fastapi import FastAPI
import openai
import os

app = FastAPI()
openai.api_key = os.environ["OPENAI_API_KEY"]

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
    import uvicorn
    uvicorn.run(app, host="100.103.8.45", port=5000)