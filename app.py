from flask import Flask, request, jsonify, Response, make_response, render_template
from config import Config
from db import db
from routes.itemBlueprint import itemBp
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=Config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

# Import the models (must be done after initializing the app)
from models.Item import Item

with app.app_context():
    db.create_all()
    db.session.commit()

# Register a root route
@app.route("/", methods=["get"])
def home():
    items = Item.query.order_by(desc(Item.date)).all()
    return render_template('home.html', items=items)

# Register the item routes as /item/*
app.register_blueprint(itemBp, url_prefix="/item")

# Start the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=Config.PORT, debug=True)
