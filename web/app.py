from flask import Flask, render_template
app = Flask(__name__)
import os

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(threaded=True, port=os.environ['PORT'])
