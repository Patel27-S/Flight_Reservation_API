from flask import Blueprint, jsonify
from models import Flight

flight = Blueprint('flight', __name__)


@flight.route('/FindFlights/<departure_city>/<arrival_city>/<date_of_departure>', methods = ['GET','POST'])
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


@flight.route('/flight/<airline>', methods = ['GET'])
def listing_flight(airline):

    try:
        list = [i for i in Flight.query.filter(airline=airline)]
    except Exception:
        return jsonify({'Airline': 'No such airline found.'})

    return jsonify({'airline': list})