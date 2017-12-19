# Main module entry point
from EltechAssistant import BotWebhook

from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        BotWebhook.BotWebhook.write_json(data)
        message = BotWebhook.BotWebhook.get_message(data)
        chat_id = message['chat_id']
        text = message['text']
        if 'hi' in text:
            BotWebhook.BotWebhook.send_message(chat_id, text)
        else:
            BotWebhook.BotWebhook.send_message(chat_id)
        return jsonify(data)
    pass


if __name__ == '__main__':
    app.run()