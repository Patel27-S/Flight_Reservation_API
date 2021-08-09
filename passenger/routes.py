from flask import Blueprint, jsonify
from models import Passenger

passenger = Blueprint('passenger', __name__)

@passenger.route('/passenger', methods = ['GET'])
def listing_passengers():
    list = [i for i in Passenger.query.all()]
    return jsonify({'Passengers': list})


