from fastapi import FastAPI, Request
import uvicorn
import requests
import json


app = FastAPI()

@app.post('/gpt')
async def gpt(request: Request):
    data = await request.form()
    dictData = dict(data)
    print("Received command:", data)

    #チャンネルIDから履歴を取得
    # channel_id = jsondata.get('channel_id')
    # print ("Channel_id = " + channel_id)
    # history = getPostsHistory(channel_id)
    
    #履歴と問い合わせを結合
    #query = jsondata.get()

    #辞書化したデータを一覧表示
    for key in dictData:
        print(key, dictData[key])

    response = {
        "response_type": "in_channel",  # "in_channel" or "ephemeral"
        "text": "コマンドを受け取りました: {}".format(data.get('text'))
    }
    return response

# チャンネルの投稿履歴を取得します。
def getPostsHistory(ChennelId):
    response = requests.get(f'{base_url}/channels/{channel_id}/posts', headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content)
        formatted_json = json.dumps(data, indent=4,ensure_ascii=False)
        return formatted_json
    else:
        return ('Error:', response.status_code)

if __name__ == '__main__':
    uvicorn.run(app, host='100.103.8.45', port=5000, reload=True)