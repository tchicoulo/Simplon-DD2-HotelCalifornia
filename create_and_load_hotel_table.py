import psycopg2
from Hotel import Hotel

# my DB
conn = psycopg2.connect(dsn="postgres://idvyhchr:FIamlsoJmMTJToQO-ysWzNWjo5gSMEL3@manny.db.elephantsql.com:5432/idvyhchr")
# data DB
conn1 = psycopg2.connect (dsn="postgres://fznuqzso:ayBfiv2zdC6_wJJ8hqqMWnsKpetsLsXc@manny.db.elephantsql.com:5432/fznuqzso")
cur1 = conn1.cursor()

# Hotel table creation
Hotel.create_table(conn)

# Hotel table data load
rows = []
cur1.execute("""SELECT * FROM hotel""")
for row in cur1:
    hotel = Hotel(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    hotel.load(conn)

conn.commit()
conn1.close()
conn.close()
