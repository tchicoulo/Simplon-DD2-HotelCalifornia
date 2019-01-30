import psycopg2
from Client import Client

# my DB
conn = psycopg2.connect(dsn="postgres://idvyhchr:FIamlsoJmMTJToQO-ysWzNWjo5gSMEL3@manny.db.elephantsql.com:5432/idvyhchr")

# Client table creation
Client.create_table(conn)

conn.commit()
conn.close()
