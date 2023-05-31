#!/usr/bin/python3

import openai
import configparser

config = configparser.ConfigParser()
config.read('../../smart_speaker.conf')
openai.api_key = config.get('dialogflow', 'openai_api_key')

messages = []

message = "樹莓派可以吃嗎？" 
print(message)

if message:
    messages.append(
        {"role": "user", "content": message},
    )   
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )   
    
reply = chat.choices[0].message
