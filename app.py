# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_pymongo import PyMongo, ObjectId
from flask_bootstrap import Bootstrap
from datetime import datetime
from models import *
import random, json, config

# Init processes
app = Flask(__name__)
Bootstrap(app)
app.config['MONGO_URI'] = config.mongoDBURL
mongo = PyMongo(app)

# Routes
@app.route('/')
def index():
	# We are hardcoding this to be our one toy flight
    session['flightid'] = config.flightID
    return render_template('index.html')


# Stores information about passenger in the session for global use
@app.route('/welcome', methods=['GET','POST'])
def welcome():
	if (request.method == 'POST'):
		conf = request.form['conf']
		found_passenger = mongo.db.passengers.find_one({'confirmation':conf})
		if found_passenger is not None:
			temp = {'name': found_passenger['name'],
					'seat': found_passenger['seat']}
			session['passenger'] = temp
			staff = mongo.db.staff.find({"flightid": ObjectId(session['flightid'])})
		else:
			flash('Confirmation number not found.')
			return redirect(url_for('index'))
	if 'flightid' in session:
	    return render_template('welcome.html', name = session['passenger']['name']['first'], seat = session['passenger']['seat'])
	else:
		return redirect(url_for('index'))

# Gets Staff info from the db, as staff might be different each flight
@app.route('/team', methods=['GET'])
def team():
	# Pull all the staffs that have the current flightid
	staff_res = (mongo.db.staff.find({"flightid": ObjectId(session['flightid'])}))
	staff = []
	for person in staff_res:
		staff.append(person)

	return render_template('team.html', staffmembers = staff, name = session['passenger']['name']['first'], seat = session['passenger']['seat'])

# Request page
@app.route('/requests')
def requests():
	staff_res = (mongo.db.staff.find({"flightid": ObjectId(session['flightid'])}))
	staff = []
	for person in staff_res:
		staff.append(person)

	# Passes the JSON file with the list of in-flight items to requests.html	
	data = json.load(open('static/items.json'))

	return render_template('requests.html', data=data, staffmembers = staff, staff_member = 'Lizzie',name = session['passenger']['name']['first'], seat = session['passenger']['seat'])

@app.route('/submit-request', methods=['POST'])
def submit_request():
    formdata = request.form
    # person = 'Lizzie' #TODO: fix it
    # seat = session['passenger']['seat']
    # flash('Your request has been received! ' + person + ' will be by seat ' + seat + ' shortly.')

    return redirect(url_for('welcome'))

@app.route('/feedback')
def feedback():
	# Pull all the staffs that have the current flightid
	staff_res = (mongo.db.staff.find({"flightid": ObjectId(session['flightid'])}))
	staff = []

	for person in staff_res:
		staff.append(person)
		
	return render_template('feedback.html', staffmembers = staff, name = session['passenger']['name']['first'], seat = session['passenger']['seat'])

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    formdata = request.form

    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.config["SECRET_KEY"] = config.secretKey
    app.run('localhost', 8080, debug=True)