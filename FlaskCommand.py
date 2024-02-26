from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/gpt', methods=['POST'])
def slash_command():
    data = request.form
    print("Received command:", data)
    # ここで受け取ったコマンドを処理します
    response = {
        "response_type": "in_channel",  # "in_channel" or "ephemeral"
        "text": "コマンドを受け取りました: {}".format(data.get('text'))
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='100.103.8.45')
