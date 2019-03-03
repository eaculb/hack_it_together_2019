# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_pymongo import PyMongo, ObjectId
from datetime import datetime
from models import *
import json

# Init processes

app = Flask(__name__)
# app.register_error_handler(404, page_not_found)
app.config['MONGO_URI'] = "mongodb://eac:sfmlab1107@ds159025.mlab.com:59025/hackit_jetblue"
mongo = PyMongo(app)

# Routes
@app.route('/')
def index():
    session['flightid'] = "5c7c21f3dd5f613e4b3baf40"
    return "<h1>You did it!</h1><p>" + session['flightid'] + "</p>"


# Stores information about passenger in the session for global use
@app.route('/welcome', methods=['POST'])
def welcome():
    conf = requests.form.confirmation 
    session['passenger'] = Passengers.get(confirmation = conf)
    return render_template('welcome.html', passenger = session['passenger'])

# Gets Staff info from the db, as staff might be different each flight
@app.route('/team', methods=['GET'])
def team():
	# Pull all the staffs that have the current flightid
	staff = list(mongo.db.staff.find({"flightid": ObjectId[session['flightid']]}))

	# session["flight"] = Flight.get(flightid)
	return render_template('team.html', staff = staff)

@app.route('/testpilot')
def testpilot():
	return render_template('pilot.html', rating = 5, years_of_experience = 5, number = 6, pilotname = 'bob', hometown = 'NYC', languages = ['English'], funfact = 'i like turtles')

@app.route('/requests')
def requests():
    return render_template('requests.html', seat='19F', staff_member = 'Bob')

@app.route('/submit-request', methods=['POST'])
def submit_request():
    formdata = request.form
    flash('Your request has been received! {{name}} will be by seat {{seat}} shortly.')

    return redirect(url_for('requests'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.config["SECRET_KEY"] = "hackit!!!"
    app.run('localhost', 8080, debug=True)