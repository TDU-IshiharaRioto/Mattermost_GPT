from fastapi import FastAPI, Request
import uvicorn
import requests
import json

base_url = 'https://cci.trial.inl.aj.dendai.ac.jp/api/v4'
api_token = '1pbn84itmjf9bp79txsgn8iwfw'


app = FastAPI()

@app.post('/gpt')
async def gpt(request: Request):
    data = await request.form()
    dictData = dict(data)
    print("Received command:", data)

    #チャンネルIDから履歴を取得
    channel_id = dictData.get('channel_id')
    print ("送信元Channel_idは、" + channel_id)
    history = getPostsHistory(channel_id)
    
    #履歴を表示
    print(history)

    #辞書化したデータを一覧表示
    # for key in dictData:
    #     print(key, dictData[key])
    # 結果
    # channel_id owxrkonrcjbkfkk6i7pnqtfmwh
    # channel_name gpttest
    # command /gpt
    # response_url https://cci.trial.inl.aj.dendai.ac.jp/hooks/commands/6rm3n3ddcpdo7xjca7ih5zjk6r
    # team_domain operation
    # team_id czro41sdc3nz7kso7pscw5dpch
    # text こんにちは。
    # token macmo7pmjjgu8jcxmeo6joksde
    # trigger_id emJrOGtiZGU3cHJzdGN3NGM2NW9hb2gzaWM6OGU0ZzU2MzF6amdxdXA4cjNkMTExNzloN2E6MTcwODk0MDQwMjY2OTpNRVVDSVFDQnZUamoyS24xZnZHcmpES1RhTDNsaEI3YUZiL2N5TTRLeHhhN1JKT3M2QUlnQXVYVGZLK21nYTZSRnZlM0owZWlWTEFVOVpGKzVMMm54WWFORzJObTBRcz0=
    # user_id 8e4g5631zjgqup8r3d11179h7a
    # user_name ishihararioto

    #履歴と問い合わせを結合
    #query = history + dictData.get('text')

    #OpenAIに問い合わせる

    response = {
        "response_type": "in_channel",  # "in_channel" or "ephemeral"
        "text": "コマンドを受け取りました: {}".format(data.get('text'))
    }
    return response

# チャンネルの投稿履歴を取得します。
def getPostsHistory(ChannelId):
    response = requests.get(f'{base_url}/channels/{ChannelId}/posts', headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content)
        formatted_json = json.dumps(data, indent=4,ensure_ascii=False)
        return formatted_json
    else:
        return ('Error:', response.status_code)

if __name__ == '__main__':
    uvicorn.run(app, host='100.103.8.45', port=5000, reload=True)