import pandas as pd
import random
from passenger.models import Passenger, db


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

    passenger = Passenger(flight_id  = single_row_2[0], first_name = single_row_2[1], last_name = single_row_2[2], \
        email = single_row_2[3], phone_number = single_row_2[4])

    db.session.add(passenger)
    db.session.commit()