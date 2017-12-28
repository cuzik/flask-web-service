from flask import Flask, request
from flask_restful import Api, Resource
import back_end as bd

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
      bd.insert_product(values)
    except Exception as e:
      return {'error': str(e)}
    return [{'success': 'this product was included'}, values]



api.add_resource(Info, '/', '/info')
api.add_resource(InsertProduct, '/add/<string:prd_cod>/<string:prd_name>/<string:prd_description>/<string:prd_price>/<string:prd_stock>')

if __name__ == '__main__':
    app.run(debug=True)



