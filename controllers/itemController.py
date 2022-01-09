from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from models.Item import Item
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import datetime
from db import db

# POST /item/create
def create():
    data = request.json
    item = Item(
        name = data.get("name"),
        type = data.get("type"),
        stock = data.get("stock"),
        description = data.get("description"),
        date = datetime.datetime.now()
    )
    db.session.add(item)
    db.session.commit()
    return f"Successfully created item {item.id}"

# DELETE /item/delete
# Delete an item by id
def delete():
    data = request.json
    id = data.get("id")
    Item.query.filter_by(id=id).delete()
    db.session.commit()
    return f"Successfully deleted {id}"

# PATCH /item/update
# Update an item by id
def update():
    data = request.json
    id = data["id"]
    item = Item.query.get(id)
    for key in data.keys():
        setattr(item, key, data[key] if key in data else getattr(item, key))
    db.session.commit()
    return "Successfully updated item"

# GET /item/list
# List all items
# Response is an array of json serialized rows
def list():
    result = Item.query.order_by(Item.date).all()
    resultJson = [x.serialize for x in result]
    return jsonify(resultJson)
