import pandas as pd
import random
import datetime as dt
from flight_reservation_api import Flight, Passenger, Reservation, db


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

random_dates_departure = [dt.date(2021, 7, 18), dt.date(2021, 7, 19), dt.date(2021, 7, 23), dt.date(2021, 7, 28),\
     dt.date(2021, 9, 20), dt.date(2021, 7, 15)]

for row in range(len(df.index)):
    df['date_of_departure', row] = random.choice(random_dates_departure)

# Making the table for departure_time:

random_times_departure = [dt.time(10, 45, 21), dt.time(11,45,57), dt.time(18, 12, 23), dt.time(20, 15, 45), dt.time(15, 12, 32), \
    dt.time(22, 12, 23), dt.time(18, 30, 40)]

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


# Now, let us fill up the 'Passenger' model:

df_2 = pd.DataFrame()

for row in range(1,21):
    df_2['flight_id', row] =  row

first_names = ['Smit', 'Chris', 'Digant', 'Karan', 'Kaman', 'Jay', 'Hardik', 'Paresh', 'Mike', 'Tom']
last_names = ['Shah', 'Patel', 'Goradia', 'Jivani', 'Ponting', 'Johnson', 'Siddle', 'Tank', 'Jani']


for row in range(len(df_2.index)):
    df_2['first_name', row] = random.choice(first_names)

for row in range(len(df_2.index)):
    df_2['last_name', row] = random.choice(last_names)

count_2 = 2
for row in range(len(df_2.index)):
    df_2['email', row] = count_2 +1

count_2 = 3
for row in range(len(df_2.index)):
    df_2['phone_number', row] = count_2 +1

index_2 = df_2.index
no_of_rows_2 = len(index_2)

for row in range(no_of_rows_2):
    single_row_2 = df_2.iloc[[row]]

    passenger = Passenger(flight_id  = single_row[0], first_name = single_row[1], last_name = single_row[2], \
        email = single_row[3], phone_number = single_row[4])

    db.session.add(passenger)
    db.session.commit()

# Filling up the 'Reservation' model:

df_3 = pd.DataFrame()

for row in range(1,21):
    df_3['flight_number', row] = row
    df_3['passenger_id', row] = row

index_3 = df_3.index
no_of_rows_3 = len(index_3)

for row in range(no_of_rows_3):
    single_row_3 = df_3.iloc[[row]]

    reservation = Reservation(flight_number = single_row_3[0], passenger_id = single_row[1])

    db.session.add(reservation)
    db.session.commit()