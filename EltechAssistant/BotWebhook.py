import requests
import json
import misc

from flask import Flask
from flask import request
from flask import jsonify

class BotWebhook:
    token = misc.token
    URL = 'https://api.telegram.org/bot' + token + '/'
    def __init__(self):
        pass
    def write_json(data, filename='updates.json'):
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    def get_message(data):
        chat_id = data['message']['chat']['id']
        text = data['message']['text']
        message = {'chat_id': chat_id, 'text': text}
        return message
    def send_message(chat_id, text='I don\'t understand you'):
        url = BotWebhook.URL + 'sendMessage'
        answer = {'chat_id': chat_id, 'text': text}
        r = requests.post(url, json=answer)
        return json

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        BotWebhook.write_json(data)
        message = BotWebhook.get_message(data)
        chat_id = message['chat_id']
        text = message['text']
        if 'hi' in text:
            BotWebhook.send_message(chat_id, text)
        else:
            BotWebhook.send_message(chat_id)
        return jsonify(data)
    return '<h1>Привет! </h1>'

if __name__ == '__main__':
    app.run()

