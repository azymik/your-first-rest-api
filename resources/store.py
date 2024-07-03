import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema


blp = Blueprint('stores', __name__, description='Operations on stores')


@blp.route('/store/<string:store_id>')
class Store(MethodView):
    # FIXME: http GET :5000/store/[STORE_ID]
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message='Store not found.')

    # FIXME: http DELETE :5000/store/[store_id]
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {'message': 'Store deleted.'}
        except KeyError:
            abort(404, message='Store not found.')


@blp.route('/store')
class StoreList(MethodView):
    # FIXME: http GET :5000/store
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    # FIXME: http POST :5000/store name='My Store 2'
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data['name'] == store['name']:
                abort(400, message=f'Store already exists.')
        store_id = uuid.uuid4().hex
        store = {
            **store_data,
            'id': store_id,
        }
        stores[store_id] = store
        return store
