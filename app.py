from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'Chair',
                'price': 15.99,
            },
        ],
    },
]


@app.get('/store')  # http://localhost:65000/store
def get_stores():
    return {'stores': stores}

@app.post('/store') # http://localhost:6500/store name='my store' 
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': [],
    }
    stores.append(new_store)
    return new_store, 201

@app.post('/store/<string:name>/item') # http http://localhost:5000/store/My\ Store/item name='Table' price:=17.99
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
            }
            store['items'].append(new_item)
            return new_item, 201
    return {'message': 'Store not found'}, 404