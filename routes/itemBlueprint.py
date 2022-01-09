from flask import Blueprint
from controllers.itemController import create, delete, list, update


itemBp = Blueprint('item', __name__, url_prefix='/item')

itemBp.route('/create', methods=['POST'])(create)
itemBp.route('/delete', methods=['DELETE'])(delete)
itemBp.route('/list', methods=['GET'])(list)
itemBp.route('/update', methods=['PATCH'])(update)
