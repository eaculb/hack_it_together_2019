#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import *
from datetime import datetime

from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_mongoengine import MongoEngine, ObjectId

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)

lizzie_dict = {
	'name' : 'Elizabeth Culbertson',
	'role' : 'cabin crew',
	'startdate' : datetime(2018, 6, 2, 12, 00),
	'languages' : ['English', 'Español'],
	'hometown' : 'Vienna, VA',
	'funfact' : 'I sing barbershop!',
	'photourl' : 'https://avatars0.githubusercontent.com/u/31480498?s=460&v=4',
	'flightid' : '0001'
}

lizzie = Staff(*lizzie_dict).save()

# jimmy_dict = {
# 	'name' : 'Jimmy Bobbertson'
# 	'role' : 'cabin crew'
# 	'startdate' : datetime(2016, 11, 17, 12, 00)
# 	'languages' : ['English', 'Español', 'Deu']
# 	'hometown' : 'Vienna, VA'
# 	'funfact' : 'I sing barbershop!'
# 	'photourl' : 'https://avatars0.githubusercontent.com/u/31480498?s=460&v=4'
# 	'flightid' : '0001'
# }

# lizzie_dict = {
# 	'name' : 'Kelly Personson'
# 	'role' : 'cabin crew'
# 	'startdate' : datetime(2018, 6, 2, 12, 00)
# 	'languages' : ['English', 'Español']
# 	'hometown' : 'Vienna, VA'
# 	'funfact' : 'I sing barbershop!'
# 	'photourl' : 'https://avatars0.githubusercontent.com/u/31480498?s=460&v=4'
# 	'flightid' : '0001'
# }

# lizzie_dict = {
# 	'name' : 'Elizabeth Culbertson'
# 	'role' : 'cabin crew'
# 	'startdate' : datetime(2018, 6, 2, 12, 00)
# 	'languages' : ['English', 'Español']
# 	'hometown' : 'Vienna, VA'
# 	'funfact' : 'I sing barbershop!'
# 	'photourl' : 'https://avatars0.githubusercontent.com/u/31480498?s=460&v=4'
# 	'flightid' : '0001'
# }