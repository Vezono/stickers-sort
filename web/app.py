from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__)
import os
import requests

import hashlib
import redis
import urllib.parse as urlparse
redis_url = os.getenv('REDISTOGO_URL')
urlparse.uses_netloc.append('redis')
url = urlparse.urlparse(redis_url)
r = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)

import web.config as config
from telebot import TeleBot
bot = TeleBot(config.token)

from pymongo import MongoClient

db = MongoClient(config.database)
users = db.stickers.users

domain = 'http://lk-contest.herokuapp.com'

app.secret_key = 'UFHEuonhBWSIHfANJ:BFueojfb!wbeofipjmnv'

@app.route('/', methods=['GET'])
def hello_world():
    user_id = request.args.get('id')
    key = request.args.get('session')
    if not user_id or not key:
        return 'Вы не вошли в систему. Получите ссылку в боте командой /login'
    if not check_user(user_id, key):
        return 'У ссылки истек срок действия или она повреждена.'
    session['id'] = user_id
    #return f'Вход успешен! {domain + url_for("logout")} - выйти из системы {domain + url_for("main_page")} - главная'
    return render_template('succsesfull_login.html', domain=domain, url_for=url_for)

@app.route('/logout')
def logout():
    # удалить из сессии имя пользователя, если оно там есть
    session.pop('id', None)
    return redirect(domain)

@app.route('/main')
def main_page():
    user_id = int(session["id"])
    stickers = get_stickers(user_id)
    imgs = []
    for sticker in stickers:
        number = sticker.split('stickers/')[1]
        img = get_file(sticker, number)
    return render_template('main.html', stickers=imgs)
        
    
    
    
def check_user(user_id, key):
    salted = user_id + r.get('salt').decode("utf-8")
    true_key = hashlib.md5(salted.encode()).hexdigest()
    return (key == true_key)
    
    
def get_file(url, name):
    r = requests.get(url)
    out = open(f"res\\{name}", "wb")
    out.write(p.content)
    out.close()
    return f'res/{name}.png'



def get_stickers(user_id):
    user = users.find_one({'id': user_id})
    stickers = []
    for category in user['stickers']:
        for sticker in user['stickers'][category]:
            stickers.append(bot.get_file_url(sticker))
    return stickers
        
if __name__ == "__main__":
    app.run(threaded=True, port=os.environ['PORT'])
    
