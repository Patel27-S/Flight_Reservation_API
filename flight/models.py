from flask_sqlalchemy import SQLAlchemy
from .routes import flight

db = SQLAlchemy(flight)



class Flight(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    number = db.Column(db.Integer)
    airline = db.Column(db.String(100))
    departure_city = db.Column(db.String(100))
    arrival_city = db.Column(db.String(100))
    date_of_departure = db.Column(db.Date)
    departure_time = db.Column(db.Date)
    
    reservartion = db.relationship('Reservation', backref = 'flight', lazy = 'dynamic')
    
    passenger = db.relationship('Passenger', backref = 'flight', lazy = 'dynamic')

    def __repr__(self):
        return '<Flight - {}>'.format(Flight.airline)