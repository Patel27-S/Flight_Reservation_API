from .routes import passenger 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(passenger)


class Passenger(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flight.id'))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique = True)
    phone_number = db.Column(db.Integer, unique = True)
    
    reservation = db.relationship('Reservation', backref = 'passenger', lazy = 'dynamic')


    def __repr__(self):
        return ' <Passenger - {} {} , {}>'.format(Passenger.first_name, Passenger.last_name, Passenger.email)



