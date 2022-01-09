from flask import Blueprint
from controllers.itemController import create, delete, list, update, export


itemBp = Blueprint('item', __name__, url_prefix='/item')

itemBp.route('/create', methods=['POST'])(create)
itemBp.route('/delete/<string:itemId>', methods=['POST'])(delete)
itemBp.route('/list', methods=['GET'])(list)
itemBp.route('/update/<string:itemId>', methods=['POST'])(update)
itemBp.route('/export', methods=['GET'])(export)
