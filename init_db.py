import configparser

import Facade

conn = Facade.get_connection()
data_conn = Facade.get_data_connection()

Facade.reset_DB()

conn.commit()
conn.close()

data_conn.close()
