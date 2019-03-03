# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_mongoengine import MongoEngine, ObjectId

# Init processes

app = Flask(__name__)

# Routes

@app.route('/')
def index():
    return render_template('empty.html', user = checkUser(), img=getUserImg())

if __name__ == '__main__':
    app.run('localhost', 8080, debug=True)