#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dashboard')
def index():
    return render_template('index.html')

@app.route('/receipt')
def receipt():
    return render_template('receipt.html')

@app.route('/signup')
def create():
    return render_template('create.html')

@app.route('/signin')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
