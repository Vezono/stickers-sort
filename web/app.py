from flask import Flask, render_template, request, session, url_for
app = Flask(__name__)
import os

import hashlib
import redis
import urllib.parse as urlparse
redis_url = os.getenv('REDISTOGO_URL')
urlparse.uses_netloc.append('redis')
url = urlparse.urlparse(redis_url)
r = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)

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
    return f'Вход успешен! {url_for("/logout")} - выйти из системы {url_for("/main")} - главная'

@app.route('/logout')
def logout():
    # удалить из сессии имя пользователя, если оно там есть
    session.pop('id', None)
    return redirect(url_for('/'))

@app.route('/main')
def main_page():
    return f'Ваш айди  - {session['id']}'

def check_user(user_id, key):
    salted = user_id + r.get('salt').decode("utf-8")
    true_key = hashlib.md5(salted.encode()).hexdigest()
    return (key == true_key)
    
if __name__ == "__main__":
    app.run(threaded=True, port=os.environ['PORT'])
    
