class Country:

  def __init__(self, code, name):
    self.code = code
    self.name = name

  def create_table(conn):
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS country (id CHARACTER(2) PRIMARY KEY,name TEXT NOT NULL)""")

  def load(self, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO country (id, name) VALUES(%s, %s)", (self.code, self.name))
        
  def reset_table(conn):
    Country.create_table(conn)

    f = open("codes_pays.txt","r")

    for line in f:
      l = line.split("\t")
      country = Country(l[1], l[0])
      country.load(conn)

    f.close()

  def drop_table(conn):
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS country")

