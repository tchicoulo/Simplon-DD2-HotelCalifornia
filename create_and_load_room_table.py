import psycopg2
from Room import Room

# my DB
conn = psycopg2.connect(dsn="postgres://idvyhchr:FIamlsoJmMTJToQO-ysWzNWjo5gSMEL3@manny.db.elephantsql.com:5432/idvyhchr")
# data DB
conn1 = psycopg2.connect (dsn="postgres://fznuqzso:ayBfiv2zdC6_wJJ8hqqMWnsKpetsLsXc@manny.db.elephantsql.com:5432/fznuqzso")
cur1 = conn1.cursor()

# Room table creation
Room.create_table(conn)

# Room table data load
rows = []
cur1.execute("""SELECT * FROM room""")
for row in cur1:
    room = Room(row[0],row[1],row[2],row[3])
    room.load(conn)

conn.commit()
conn1.close()
conn.close()
