from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


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


class Reservation(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    flight_number = db.Column(db.Integer, db.ForeignKey('flight.number'))
    passenger_id = db.Column(db.Integer, db.ForeignKey('passenger.id'))

    def __repr__(self):
        return '<Reservation - {} {}>'.format(Reservation.flight_number, Reservation.passenger_id)


 
# Below are all the routes/endpoints for finding flights, saving, updating and deleting reservations :

@app.route('/home', methods = ['GET'])
def index():
    return 'Hello World! I am building an API.'  
        
@app.route('/FindFlights/<departure_city>/<arrival_city>/<date_of_departure>', methods = ['GET','POST'])
def find_flights(departure_city, arrival_city, date_of_departure):
    flights = Flight.query.filter_by(departure_city = departure_city, arrival_city = arrival_city,\
                   date_of_departure = date_of_departure)
    # If a flight with the departure_city, arrival_city, date_of_departure requested,
    # does not exist in the database, then we are :
    if not flights:
        return jsonify({'flights': 'None with the entered data. Sorry!'})
    else:
        # Else, if a list of such flights is found in the database, then we return the JSON version
        # in response.
        return jsonify({'flights': flights})

@app.route('/SaveReservation/<first_name>/<last_name>/<email>/<phone_number>', methods = ['GET','POST'])
def save_reservation(first_name, last_name, email, phone_number):
   
   passenger = Passenger(first_name = first_name, last_name = last_name, email = email, phone_number = phone_number)
   reservation = Reservation(flight_number = Reservation.flight.number , passenger_id =  Reservation.passenger.id)
   db.session.add(passenger)
   db.session.add(Reservation)
   db.session.commit()
   return jsonify({'201': 'Reservation Successfull!'})


@app.route('/DeleteReservations/<passenger_id>/<flight_num>', methods = ['POST', 'DELETE', 'GET'])
def delete_reservation(passenger_id, flight_num):
    
    reservation = Reservation(passenger_id = passenger_id, flight_num = flight_num)

    # If no such reservation exists, then :

    if not reservation:
        return jsonify({'Delete_Reservation': 'No such reservation exists.'})

    # Else, we delete the reservation :
    else:
        db.session.delete(reservation)
        db.session.commit()
        return jsonify({'Deleted_Reservation': 'The reservation has been successfully deleted.'})


@app.route('/UpdateReservation/<current_first_name>/<current_last_name>/<current_email>/<current_phone_number>/<current_flight_number>\
                              /<new_first_name>/<new_last_name>/<new_email>/<new_phone_number>,<new_flight_number>', methods = ['PUT', 'POST', 'GET'])

def update_reservation(current_first_name, current_last_name, current_email, current_phone_number, current_flight_number,\
                       new_first_name, new_last_name, new_email, new_phone_number, new_flight_number):
    
    # First of all we will check if such a reservation is existing:
    passenger = Passenger(first_name = current_first_name, last_name = current_last_name, email = current_email, phone_number = current_phone_number)
    
    reservation = Reservation(flight_number = current_flight_number, passenger_id = Reservation.query.filter_by(flight_number = current_flight_number).passenger_id)
    
    if passenger and reservation:
    
        db.session.delete(passenger)
        db.session.delete(reservation)
        db.session.commit()
         
       # Now, we will update the passenger and reservation tables with the updated details : 
       
        updated_passenger = Passenger(first_name = new_first_name, last_name = new_last_name, email = new_email, phone_number = new_phone_number)
        
        updated_reservation = Reservation(flight_number = new_flight_number, passenger_id = Passenger.query.filter_by(email = new_email).id )
        
        db.session.add(updated_passenger)
        db.session.add(updated_reservation)
        db.session.commit()
        
        return jsonify({'Reservation': 'Updated'})
   
    else:
        
        return jsonify({'Reservation': 'No such reservation exists.'})




# Below are all the routes/endpoints for listing :

@app.route('/flight/<airline>', methods = ['GET'])
def listing_flight(airline):

    try:
        list = [i for i in Flight.query.filter(airline=airline)]
    except Exception:
        return jsonify({'Airline': 'No such airline found.'})

    return jsonify({'airline': list})

	
@app.route('/passenger', methods = ['GET'])
def listing_passengers():
    list = [i for i in Passenger.query.all()]
    return jsonify({'Passengers': list})


@app.route('/reservation', methods = ['GET'])
def listing_reservation():
    list = [i for i in Reservation.query.all()]
    return jsonify({'Reservation': list})

