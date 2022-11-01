from flask import Flask, request
app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    return '<p>Welcome</p>'


@app.route('/welcome/home')
def say_welcome_home():
    return '<p>Welcome home</p>'


@app.route('/welcome/back')
def say_welcome_back():
    return '<p>Welcome back</p>'


