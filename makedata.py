#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import *
from datetime import datetime

# cabin crew
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

# cabin crew
lyn_dict = {
	'name' : 'Lynoska Garcia',
	'role' : 'cabin crew',
	'startdate' : datetime(2018, 6, 3, 12, 00),
	'languages' : ['English', 'Español', 'Portuguese'],
	'hometown' : 'Dominican Republic',
	'funfact' : 'I read, a lot. Way too much.',
	'photourl' : 'https://avatars0.githubusercontent.com/u/31480498?s=460&v=4',
	'flightid' : '0001'
}

lyn = Staff(*lyn_dict).save()

# cabin crew
fabliha_dict = {
	'name' : 'Fabliha Hossain',
	'role' : 'cabin crew',
	'startdate' : datetime(2018, 4, 2, 12, 00),
	'languages' : ['English', 'Bangali'],
	'hometown' : 'Bangledash',
	'funfact' : 'Im a CS major with an English minor',
	'photourl' : 'https://avatars0.githubusercontent.com/u/31480498?s=460&v=4',
	'flightid' : '0001'
}

fabliha = Staff(*fabliha_dict).save()

# cabin crew
vicky_dict = {
	'name' : 'Victoria Grinthal',
	'role' : 'cabin crew',
	'startdate' : datetime(2018, 5, 2, 12, 00),
	'languages' : ['English'],
	'hometown' : 'Copiague, New York',
	'funfact' : 'I have a twin brother whom I sing with',
	'photourl' : 'https://avatars0.githubusercontent.com/u/31480498?s=460&v=4',
	'flightid' : '0001'
}

vicky = Staff(*vicky_dict).save()

# pilot info
pilot_dict = {
	'name' : 'Mr. Pilot',
	'role' : 'pilot',
	'startdate' : datetime(2018, 6, 2, 12, 00),
	'languages' : ['English'],
	'hometown' : 'Austin, Texas',
	'funfact' : 'I can play the guitar with my feet',
	'photourl' : 'https://avatars0.githubusercontent.com/u/31480498?s=460&v=4',
	'flightid' : '0001'
}

pilot = Staff(*pilot_dict).save()
