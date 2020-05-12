from flask import Flask, render_template, request
app = Flask(__name__)
import os

@app.route('/', methods=['GET'])
def hello_world():
    user_id = request.args.get('id')
    key = request.args.get('session')
    if not user_id or not key:
        return 'Вы не вошли в систему. Получите ссылку в боте командой /login'
    return 'Аргументы есть!'
    #return render_template('index.html')

if __name__ == "__main__":
    app.run(threaded=True, port=os.environ['PORT'])
