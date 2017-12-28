import config

# Function that you can use
# -> insert_product(values)
# -> update_values(values)
# -> query_values(query)
#

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

def query_values(query):
  cnx = config.open_connection()
  cursor = cnx.cursor()
  cursor.execute(query)
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
  sql_update = build_sql_expression(values)
  execute_sql(sql_update, values)

def build_sql_expression(values):
  sql_update = "UPDATE product SET "
  for value in values:
    if value != "prd_cod":
      sql_update+= value + " = %(" + value + ")s, "
  sql_update+= "WHERE prd_cod = %(prd_cod)s"
  return sql_update.replace(', WHERE', ' WHERE')

# update_values({'prd_cod': 1, 'prd_name': 'Feijao', 'prd_description': 'Panelaco',    'prd_price':  5.20, 'prd_stock': 45})
