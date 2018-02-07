import misc
import requests
import json
import postgresql.driver as pg_driver
from EltechAssistant import Menu
# -*- coding: utf-8 -*-

db = pg_driver.connect(user='postgres', password='', host='localhost', database='My', port=5432)
token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'
global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    print(r.json)
    return(r.json())

def get_message():
    data = get_updates()
    current_update_id = data['result'][-1]['update_id']
    global last_update_id
    if current_update_id != last_update_id:
        last_update_id = current_update_id
        chat_id = data['result'][-1]['message']['chat']['id']
        text = data['result'][-1]['message']['text']
        message = {'chat_id':chat_id,
                    'text':text}
        return message
    return None

def send_message(chat_id, text='I don\'t understand you '):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    print(url)
    requests.get(url)

def main():
    while True:
        answer = get_message()
        if answer != None:
         chat_id = answer['chat_id']
         text = answer['text']
         array = ['Привет', 'привет', 'Hi', 'Hello', 'Bot', 'bot', 'hello', 'hi']
         array2 = ['бд']
         if 'help' in text:
            send_message(chat_id, 'Чем могу Вам помочь?')
         elif text in array:
            send_message(chat_id, 'Привет. Я твой лучший помошник')
         elif text in array2:
             h = db.query("SELECT * FROM public.table_name")
             print (h)
             send_message(chat_id, h)
             # for id, in db.prepare("SELECT id FROM public.table_name"):
             #     for name, in db.prepare("SELECT name FROM public.table_name"):
             #        send_message(chat_id, id)
             #        send_message(chat_id, name)
         else:
             send_message(chat_id)
        else:
            continue
            h = db.query("SELECT id FROM public.table_name")
            print(h)
    sleep(2)
    pass


if __name__ == '__main__':
   main()




