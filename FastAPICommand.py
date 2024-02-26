from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post('/gpt')
async def gpt(request: Request):
    data = await request.form()
    print("Received command:", data)
    response = {
        "response_type": "in_channel",  # "in_channel" or "ephemeral"
        "text": "コマンドを受け取りました: {}".format(data.get('text'))
    }
    return response

if __name__ == '__main__':
    uvicorn.run(app, host='100.103.8.45', port=5000, debug=True)