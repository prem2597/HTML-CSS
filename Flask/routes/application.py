from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/prem")
def revathi():
    return "Hello, Prem!"

@app.route("/revathi")
def prem():
    return "Hello, Revathi!"