import psycopg2
from Reservation import Reservation

# my DB
conn = psycopg2.connect(dsn="postgres://idvyhchr:FIamlsoJmMTJToQO-ysWzNWjo5gSMEL3@manny.db.elephantsql.com:5432/idvyhchr")

# Reservation table creation
Reservation.create_table(conn)

conn.commit()
conn.close()
