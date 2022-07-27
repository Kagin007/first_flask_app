from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
  {
    'name': 'My wonderful Store',
    'items': [
      {
        "name": 'My Item',
        'price': 15.99
      }
    ]
  }
]

@app.route('/') # 'http://www.google.com/maps'
def home():
  return "Hello, world!"

#POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET']) #http://127.0.0.1:5000/store/some_name
def get_store(name):
  for store in stores:
    if store["name"] == name:
      return jsonify(store)
  return jsonify({'message': 'store not found'})

#GET /store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})

#GET /store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
  pass

#GET /store/<string:name>/Item
@app.route('/store/<string:name>/item', methods=['GET']) # 'http://127.0.0.1:5000/store/some_name
def get_item_in_store(name):
  for store in stores:
    if store["name"] == store:
      return jsonify({"items": store["items"]})
    return jsonify({'message': 'store not found'})

app.run(port=5000)