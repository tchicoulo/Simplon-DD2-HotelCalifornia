import psycopg2
from Country import Country

conn = psycopg2.connect(dsn="postgres://idvyhchr:FIamlsoJmMTJToQO-ysWzNWjo5gSMEL3@manny.db.elephantsql.com:5432/idvyhchr")

Country.create_table(conn)

f = open("codes_pays.txt","r")

for line in f:
  l = line.split("\t")
  country = Country(l[1], l[0])
  country.load(conn)

f.close()

conn.commit()
conn.close()
