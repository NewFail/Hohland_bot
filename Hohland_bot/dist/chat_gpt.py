import openai
from app.config_reader import load_config

config = load_config("config/bot.ini")

api=config.DC_bot.api

openai.api_key = api


messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
def request(Message):
    message = Message
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=2048
        )
    reply = chat.choices[0].message.content

    #print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    return reply

