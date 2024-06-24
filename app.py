import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)


@app.get('/store')  # http GET :5000/store
def get_stores():
    return {'stores': list(stores.values())}


@app.post('/store')  # http POST :5000/store name=[STORE NAME]'
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {
        **store_data,
        'id': store_id,
    }
    stores[store_id] = store
    return store, 201


# http POST :5000/item name=[ITEM NAME] price:=[ITEM PRICE] store_id=[STORE_ID]
@app.post('/item')
def create_item():
    item_data = request.get_json()
    if item_data['store_id'] not in stores:
        return {'message': 'Store not found'}, 404

    item_id = uuid.uuid4().hex
    item = {
        **item_data,
        'id': item_id,
    }
    items[item_id] = item
    return item, 201


@app.get('/item')  # http GET :5000/item
def get_all_items():
    return {'items': list(items.values())}


@app.get('/store/<string:store_id>')  # http GET :5000/store/[STORE_ID]
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {'message': 'Store not found'}, 404


@app.get('/item/<string:item_id>')  # http GET :5000/item/[item_id]
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {'message': 'Item not found'}, 404
