class Hotel:

  def __init__(self, id, country, address, postcode, town, stars, opened):
    self.id = id
    self.country = country
    self.address = address
    self.postcode = postcode
    self.town = town
    self.stars = stars
    self.opened = opened

  def create_table(conn):
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS hotel (
      id INTEGER PRIMARY KEY,
      country CHARACTER(2) NOT NULL,
      address TEXT NOT NULL,
      postcode TEXT NOT NULL,
      town TEXT NOT NULL,
      stars INTEGER NOT NULL,
      open SMALLINT NOT NULL
      )""")

  def load(self, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO hotel (id, country, address, postcode, town, stars, open) VALUES(%s, %s, %s, %s, %s, %s, %s)", (self.id, self.country, self.address, self.postcode, self.town, self.stars, self.opened))
    
