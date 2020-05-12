from flask import Flask
app = Flask(__name__)
import os

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(threaded=True, port=os.environ['PORT'])
