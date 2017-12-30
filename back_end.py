import config
import re

def execute_sql(sql, values):
  cnx = config.open_connection()
  cursor = cnx.cursor()
  cursor.execute(sql, values)
  cnx.commit()
  cursor.close()
  config.close_connection(cnx)

def insert_product(values):
  sql_insert = ("INSERT INTO product (prd_cod, prd_name, prd_description, prd_price, prd_stock) VALUES (%(prd_cod)s, %(prd_name)s, %(prd_description)s, %(prd_price)s, %(prd_stock)s)")
  execute_sql(sql_insert, values)

def query_values(query,values={}):
  cnx = config.open_connection()
  cursor = cnx.cursor()
  cursor.execute(query,values)
  data = []
  for (prd_cod, prd_name, prd_description, prd_price, prd_stock) in cursor:
    data+= [{
      'prd_cod': prd_cod,
      'prd_name': prd_name,
      'prd_description': prd_description,
      'prd_price': prd_price,
      'prd_stock': prd_stock
    }]
  cursor.close()
  config.close_connection(cnx)
  return data

def update_values(values):
  sql_update = build_sql_update_expression(values)
  execute_sql(sql_update, values)

def build_sql_update_expression(values):
  sql_update = "UPDATE product SET "
  for value in values:
    if value != "prd_cod":
      sql_update+= value + " = %(" + value + ")s, "
  sql_update+= "WHERE prd_cod = %(prd_cod)s"
  return sql_update.replace(', WHERE', ' WHERE')

def get_product_by(values):
  sql_query = 'SELECT * from product WHERE '
  for value in values:
    sql_query+= value + " = %(" + value + ")s AND "
  return query_values(re.sub(r" AND $", "", sql_query), values)
