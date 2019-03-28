# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_pymongo import PyMongo, ObjectId
from flask_bootstrap import Bootstrap
from datetime import datetime
import random
from models import *
from snacks_drinks import *
import json

# Init processes
app = Flask(__name__)
Bootstrap(app)
# app.register_error_handler(404, page_not_found)
app.config['MONGO_URI'] = "mongodb://eac:sfmlab1107@ds159025.mlab.com:59025/hackit_jetblue"
mongo = PyMongo(app)

# Routes
@app.route('/')
def index():
	# We are hardcoding this to be our one toy flight
    session['flightid'] = "5c7c21f3dd5f613e4b3baf40"
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
	# session["flight"] = Flight.get(flightid)
	return render_template('team.html', staffmembers = staff, name = session['passenger']['name']['first'], seat = session['passenger']['seat'])

@app.route('/requests')
def requests():
	staff_res = (mongo.db.staff.find({"flightid": ObjectId(session['flightid'])}))
	staff = []
	for person in staff_res:
		staff.append(person)
    return render_template('requests.html', staffmembers = staff, PURCHASE_LIST = PURCHASE_LIST, SNACKS_LIST = SNACKS_LIST\
    	, DRINKS_LIST = DRINKS_LIST, staff_member = 'Lizzie',name = session['passenger']['name']['first'], seat = session['passenger']['seat'])

@app.route('/submit-request', methods=['POST'])
def submit_request():
    formdata = request.form
    person = 'Lizzie' #TODO: fix it
    seat = session['passenger']['seat']
    flash('Your request has been received! ' + person + ' will be by seat ' + seat + ' shortly.')

    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.config["SECRET_KEY"] = "hackit!!!"
    app.run('localhost', 8080, debug=True)