from flask_sqlalchemy import SQLAlchemy
from .routes import reservation

db = SQLAlchemy(reservation)


class Reservation(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    flight_number = db.Column(db.Integer, db.ForeignKey('flight.number'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.id'))

    def __repr__(self):
        return '<Reservation - {} {}>'.format(Reservation.flight_number, Reservation.passenger_id)



