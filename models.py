from flask_mongoengine import MongoEngine, ObjectId

class Passenger(Document):
    name = StringField(required=True)
    confirmation = StringField(required=True)
    seat = StringField(required=True)
    flightid = ObjectId(required=True)

class Staff(Document):
    name = StringField(required=True)
    role = StringField(required=True)
    startdate = DateTimeField(required=True)
    languages = ListField(StringField(required=True))
    hometown = StringField(required=True)
    funfact = StringField(required=True)
    photo = URLField(required=True)
    flightid = ObjectIdField(required=True)

class Flight(Document):
    flightid = ObjectIdField(required=True)
    passengers = ListField(ObjectIdField(required=True))
    staff = ListField(ObjectIdField(required=True))
