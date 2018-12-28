from flask import Flask, request
import telepot
import urllib3
from mtranslate import translate

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "bot"
bot = telepot.Bot('787054665:AAFtqwvORWPfidCZTcoMJVM-4ctl8cs7N9g')
bot.setWebhook("https://botpython10.pythonanywhere.com/{}".format(secret), max_connections=1)
def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':

             x = translate(msg['text'],'fa','en')
             bot.sendMessage(chat_id,x)



app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        handle(update['message'])
    return "OK"