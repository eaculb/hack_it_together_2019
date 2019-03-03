# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_mongoengine import MongoEngine, ObjectId

# Init processes

app = Flask(__name__)
app.register_error_handler(404, page_not_found)

# Routes

@app.route('/')
def index():
    return render_template('empty.html')

@app.route('/team')
def team():
    return render_template()

@app.route('/requests')
def requests():
    return render_template()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run('localhost', 8080, debug=True)