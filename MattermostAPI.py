# トークンの説明: GPTTest
# トークンID: 7th9fbfrjpnibqgbw1h7qw1dfh
# アクセストークン: 1pbn84itmjf9bp79txsgn8iwfw

import requests
import json

base_url = 'https://cci.trial.inl.aj.dendai.ac.jp/api/v4'
api_token = '1pbn84itmjf9bp79txsgn8iwfw'

headers = {
    'Authorization': f'Bearer {api_token}',
}


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
    channel_id = 'owxrkonrcjbkfkk6i7pnqtfmwh'
    print(getPostsHistory(channel_id))
