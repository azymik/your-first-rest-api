from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema


blp = Blueprint('Items', __name__, description='Operations on items')


@blp.route('/item/<string:item_id>')
class Item(MethodView):
    # FIXME: http GET :5000/item/[item_id]
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    # FIXME: http DELETE :5000/item/[item_id]
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {'message': 'Item deleted.'}

    # FIXME: http PUT :5000/item/[item_id] name='Another Chair' price:=20.50
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data['price']
            item.name = item_data['name']
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@blp.route('/item')
class ItemList(MethodView):
    # FIXME: http GET :5000/item
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    # FIXME: http POST :5000/item name='Chair' price:=17.99 store_id:=[STORE_ID]
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):

        # if item_data['store_id'] not in stores:
        #     abort(404, message='Store not found.')

        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message='An error occured while inserting the item.')

        return item
