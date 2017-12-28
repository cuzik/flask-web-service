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

class Info(Resource):
  def get(self):
    return open("info.txt", "r").read().split('\n')

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

class UpdateProduct(Resource):
  def get(self, prd_cod, prd_name, prd_description, prd_price, prd_stock):
    values = {
      'prd_cod': prd_cod,
      'prd_name': prd_name,
      'prd_description': prd_description,
      'prd_price': prd_price,
      'prd_stock': prd_stock
    }
    try:
      db.update_values(values)
    except Exception as e:
      return {'error': str(e)}
    return [{'success': 'this product was modify'}, values]


class SelectAllProducts(Resource):
  def get(self):
    sql = "SELECT * from product"
    return db.query_values(sql)

@app.route('/info')
def instructions():
  return render_template('info.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

api.add_resource(Info, '/')
api.add_resource(InsertProduct, '/add/<string:prd_cod>/<string:prd_name>/<string:prd_description>/<string:prd_price>/<string:prd_stock>')
api.add_resource(UpdateProduct, '/upd/<string:prd_cod>/<string:prd_name>/<string:prd_description>/<string:prd_price>/<string:prd_stock>')
api.add_resource(SelectAllProducts, '/all')

if __name__ == '__main__':
    app.run(debug=True)



