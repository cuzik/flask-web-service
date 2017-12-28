from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def error_key_not_null():
  return {'error': 'key is on the system baby you cant add this key twice, try again'}

def error_key_null():
  return {'error': 'key is not on the system baby, try again'}

class Info(Resource):
  def get(self):
    return open("info.txt", "r").read().split('\n')

api.add_resource(Info, '/', '/info')

if __name__ == '__main__':
    app.run(debug=True)
