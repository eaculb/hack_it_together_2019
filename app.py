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

@app.route('/welcome', methods=['POST'])
def welcome():
    conf = requests.form.confirmation 
    session['passenger'] = Passengers.get(confirmation = conf)
    return render_template('welcome.html', passenger = session['passenger'])

@app.route('/team')
def team():
    return render_template()

@app.route('/requests')
def requests():
    return render_template('requests.html')

@app.route('/submit-request', methods=['POST'])
def submit_request():
    formdata = requests.form
    flash('Your request has been received! {{name}} will be by seat {{}} shortly.')

    return redirect(url_for('requests'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run('localhost', 8080, debug=True)