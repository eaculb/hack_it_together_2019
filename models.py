from flask_mongoengine import MongoEngine
from mongoengine import Document
from mongoengine import *

class Passenger(Document):
    name = StringField(required=True)
    confirmation = StringField(required=True)
    seat = StringField(required=True)
    flightid = ObjectIdField(required=True)

class Staff(Document):
    name = StringField(required=True)
    role = StringField(required=True)
    startdate = DateTimeField(required=True)
    languages = ListField(StringField(required=True))
    hometown = StringField(required=True)
    funfact = StringField(required=True)
    photourl = URLField(required=True)
    flightid = ObjectIdField(required=True)

class Flight(Document):
    flightid = ObjectIdField(required=True)
    passengers = ListField(ObjectIdField(required=True))
    staff = ListField(ObjectIdField(required=True))
