class Client:

  def __init__(self, email, name, firstname, nationality):
    self.email = email
    self.name = name
    self.firstname = firstname
    self.nationality = nationality

  def create_table(conn):
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS client (
      email integer NOT NULL,
      name INTEGER NOT NULL,
      firstname TEXT NOT NULL,
      nationality CHARACTER(2) NOT NULL,
      FOREIGN KEY(nationality) REFERENCES country(id),
      PRIMARY KEY (email)
    )""")

  def load(self, conn):
    cur = conn.cursor()
    cur.execute("INSERT INTO room (email, name, firstname, nationality) VALUES(%s, %s, %s, %s)", (self.email, self.name, self.firstname, self.nationality))
    
