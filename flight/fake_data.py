import pandas as pd
import random
from datetime import date as dt, time as tm
from flight.models import Flight, db


# Fake dataset for 'Flight' model of database :
# Here, we need to fill out the columns : number, airline, departure_city, arrival_city, 
# date_of_departure, departure_time.

df = pd.DataFrame()

# 'airlines' column first :

def airlines_names(size):
    airline_list = list()
    airlines = ['Air India', 'Air NZ', 'Air Australia', 'Etihad', 'Emirated', 'Qatar']
    for i in range(size):
        airline_list.append(random.choice(airlines))
    return airline_list

df['airline'] = airlines_names(20)

# 'flight_number' column :
# Now, this column should be filled in such a way that there is a only one flight_number
# for an airline.

#Below statement will generate a set containing names of all the airlines for once.
airline_set = set(airlines_names(20))

airline_dict = dict()
count = 0

# The below loop will create a dictionary in which the keys are going to be each of the airlines
# and the values are going to be unique for each of them ranging from 1 to the number of airlines.
for airline in airline_set:
    airline_dict[airline] = count +1

# The below loop will create the 'number' column. 
for i in range(len(df.index)):
    df['number', i] = airline_dict[df['airline', i]]


# Now the for the length of db.Index we have to make the 'departure_city' column.
departure_city_list = ['Canberra', 'Victoria', 'Melbourne', 'Auckland', 'Wellington', 'Christchurch', 'Hamilton', 'Perth', 'Sydney']

for i in range(len(df.index)):
    df['departure_city', i] = random.choice(departure_city_list)

# In the dataframe now for the len(db.Index) we will have to make the 'arrival_city' column.
arrival_city_list = ['Chicago', 'Ahmedabad', 'New York', 'Bengaluru', 'Washington', 'Boston', 'Jersey', 'Detroit', 'Mumbai']

for i in range(len(df.index)):
    df['arrival_city', i] = random.choice(arrival_city_list)

# Making the table for date_of_departure :

random_dates_departure = [dt(2021, 7, 18), dt(2021, 7, 19), dt(2021, 7, 23), dt(2021, 7, 28),\
     dt(2021, 9, 20), dt(2021, 7, 15)]

for row in range(len(df.index)):
    df['date_of_departure', row] = random.choice(random_dates_departure)

# Making the table for departure_time:

random_times_departure = [tm(10, 45, 21), tm(11,45,57), tm(18, 12, 23), tm(20, 15, 45), tm(15, 12, 32), \
    tm(22, 12, 23), tm(18, 30, 40)]

for row in range(len(df.index)):
    df['departure_time', row] = random.choice(random_times_departure)

# Now storing all of the values in 'flight' model.

index = df.index
no_of_rows = len(index)

for row in range(no_of_rows):
    single_row = df.iloc[[row]]

    flight = Flight(airline = single_row[0], number = single_row[1], departure_city = single_row[2], \
        arrival_city = single_row[3], date_of_departure = single_row[4], departure_time = single_row[5] )

    db.session.add(flight)
    db.session.commit()
