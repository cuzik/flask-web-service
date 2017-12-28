import mysql.connector

config = {
  'user': 'root',
  'password': 'konohamaru',
  'host': 'localhost',
  'database': 'store',
  'raise_on_warnings': True,
}

def open_connection():
  return mysql.connector.connect(**config)

def close_connection(connection):
  connection.close()
