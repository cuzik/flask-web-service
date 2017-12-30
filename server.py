from flask import Flask, request
from flask_restful import Api, Resource
from flask import render_template
import back_end as db

app = Flask(__name__)
api = Api(app)

def error_key_not_null():
  return {'error': 'key is on the system baby you cant add this key twice, try again'}

def error_key_null():
  return {'error': 'key is not on the system baby, try again'}

class InsertProduct(Resource):
  def get(self, prd_cod, prd_name, prd_description, prd_price, prd_stock):
    values = {
      'prd_cod': prd_cod,
      'prd_name': prd_name,
      'prd_description': prd_description,
      'prd_price': prd_price,
      'prd_stock': prd_stock
    }
    try:
      db.insert_product(values)
    except Exception as e:
      return {'error': str(e)}
    return [{'success': 'this product was included'}, values]

class GetProductByCod(Resource):
  def get(self, conditions):
    conditions = conditions.split(',')
    values = {}
    for i in conditions:
      i = i.split(':')
      values.update({i[0] : i[1]})
    try:
      products = db.get_product_by(values)
    except Exception as e:
      return {'error': str(e)}
    return [{'success': 'query is valid', 'count': len(products)}, products]

class UpdateProduct(Resource):
  def get(self, prd_cod, conditions):
    conditions = conditions.split(',')
    values = {'prd_cod': prd_cod}
    for i in conditions:
      i = i.split(':')
      values.update({i[0] : i[1]})
    try:
      old_values = db.get_product_by({'prd_cod': prd_cod})
      db.update_values(values)
      new_values = db.get_product_by({'prd_cod': prd_cod})
    except Exception as e:
      return {'error': str(e)}
    if(len(new_values) == 0):
      return {'error': 'product not found'}
    return [{'success': 'this product was modify'}, [{'old_values': old_values[0]}, {'new values': new_values[0]}]]


class SelectAllProducts(Resource):
  def get(self):
    sql = "SELECT * from product"
    return db.query_values(sql)

@app.route('/info')
@app.route('/')
def instructions():
  return render_template('info.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

api.add_resource(GetProductByCod, '/get/<string:conditions>')
api.add_resource(InsertProduct, '/add/<string:prd_cod>/<string:prd_name>/<string:prd_description>/<string:prd_price>/<string:prd_stock>')
api.add_resource(UpdateProduct, '/upd/<string:prd_cod>/<string:conditions>')
api.add_resource(SelectAllProducts, '/all')

if __name__ == '__main__':
    app.run(debug=True)
