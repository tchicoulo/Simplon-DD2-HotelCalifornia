import configparser
import psycopg2

from Country import Country
from Hotel import Hotel
from Room import Room
from Client import Client
from Reservation import Reservation

config = None
conn = None
data_conn = None

def reset_DB():
  conn = get_connection()

  Reservation.drop_table(conn)
  Client.drop_table(conn)
  Room.drop_table(conn)
  Hotel.drop_table(conn)
  Country.drop_table(conn)

  Country.reset_table(conn)
  Hotel.reset_table(conn)
  Room.reset_table(conn)
  Client.reset_table(conn)
  Reservation.reset_table(conn)

def get_connection():
  global conn

  if conn is None:
    conn = psycopg2.connect(dsn=get_DB_URL())

  return conn

def get_data_connection():
  global data_conn

  if data_conn is None:
    data_conn = psycopg2.connect(dsn=get_data_DB_URL())

  return data_conn

def get_name():
  global config

  if config is None:
    get_config()

  return config['DEFAULT']['MyName']

def get_DB_URL():
  global config

  if config is None:
    get_config()

  return config['elephantsql.com']['MyDBURL']

def get_data_DB_URL():
  global config

  if config is None:
    get_config()

  return config['elephantsql.com']['DataDBURL']

def get_config():
  global config

  config = configparser.ConfigParser()
  config.read('config.txt')
