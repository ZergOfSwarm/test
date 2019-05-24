from flask import Flask

app = Flask(__name__)
@app.route('/') # если после /Denis то в браузере вводить нужно будет 127.0.0..1:5000/Denis
def index():
    return"<h1>Hello Flaskers!</h1>"
