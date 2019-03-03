from flask_mongoengine import MongoEngine
from mongoengine import Document
from mongoengine import *

class Passenger():
    def __init__(self, name, confirmation, seat, flightid):
        self.name = name
        self.confirmation = confirmation
        self.seat = seat
        self.flightid = flightid
    def to_json(self):
        return {
            'name' : self.name,
            'confirmation' : self.confirmation,
            'seat' : self.seat,
            'flightid' : self.flightid
        }

class Staff():
    def __init__(self, name, role, startdate, languages, hometown, funfact, photourl, flightid):
        self.name = name
        self.role = role
        self.startdate = startdate
        self.languages = languages
        self.hometown = hometown
        self.funfact = funfact
        self.photourl = photourl
        self.flightid = flightid
    def to_json(self):
        return {
            'name' : self.name,
            'role' : self.role,
            'startdate' : self.startdate,
            'languages' : self.languages,
            'hometown' : self.hometown,
            'funfact' : self.funfact,
            'photourl' : self.photourl,
            'flightid' : self.flightid
        }

class Flight():
    def __init__(self, passengers, staff):
        self.passengers = passengers
        self.staff = staff
    def to_json(self):
        return {
            'passengers' : self.passengers,
            'staff' : self.staff
        }