from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StoreModel
from schemas import StoreSchema


blp = Blueprint('stores', __name__, description='Operations on stores')


@blp.route('/store/<string:store_id>')
class Store(MethodView):
    # FIXME: http GET :5000/store/[STORE_ID]
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    # FIXME: http DELETE :5000/store/[store_id]
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {'message': 'Store deleted.'}


@blp.route('/store')
class StoreList(MethodView):
    # FIXME: http GET :5000/store
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    # FIXME: http POST :5000/store name='My Store 2'
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message='A store with that name already exists.')
        except SQLAlchemyError:
            abort(500, message='An error occured creating the store.')

        return store
