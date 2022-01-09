from flask import Flask, request, jsonify, Response, make_response
from config import Config
from db import db
from routes.itemBlueprint import itemBp

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
def test():
    return {"message": "Shopify backend challenge!"}

# Register the item routes as /item/*
app.register_blueprint(itemBp, url_prefix="/item")

# Start the app
if __name__ == "__main__":
    app.run(port=Config.PORT, debug=True)
