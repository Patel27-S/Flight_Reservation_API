from flask import Blueprint, jsonify
from models import Reservation

reservation = Blueprint('reservation', __name__)


@reservation.route('/SaveReservation/<first_name>/<last_name>/<email>/<phone_number>', methods = ['GET','POST'])
def save_reservation(first_name, last_name, email, phone_number):
   
   passenger = Passenger(first_name = first_name, last_name = last_name, email = email, phone_number = phone_number)
   reservation = Reservation(flight_number = Reservation.flight.number , passenger_id =  Reservation.passenger.id)
   db.session.add(passenger)
   db.session.add(Reservation)
   db.session.commit()
   return jsonify({'201': 'Reservation Successfull!'})


@reservation.route('/DeleteReservations/<passenger_id>/<flight_num>', methods = ['POST', 'DELETE', 'GET'])
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



@reservation.route('/UpdateReservation/<current_first_name>/<current_last_name>/<current_email>/<current_phone_number>/<current_flight_number>\
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



@reservation.route('/reservation', methods = ['GET'])
def listing_reservation():
    list = [i for i in Reservation.query.all()]
    return jsonify({'Reservation': list})
