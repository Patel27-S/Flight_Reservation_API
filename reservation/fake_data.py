import pandas as pd
from reservation.models import Reservation, db


# Filling up the 'Reservation' model:

df_3 = pd.DataFrame()

for row in range(1,21):
    df_3['flight_number', row] = row
    df_3['passenger_id', row] = row

index_3 = df_3.index
no_of_rows_3 = len(index_3)

for row in range(no_of_rows_3):
    single_row_3 = df_3.iloc[[row]]

    reservation = Reservation(flight_number = single_row_3[0], passenger_id = single_row_3[1])

    db.session.add(reservation)
    db.session.commit()