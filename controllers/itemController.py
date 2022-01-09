from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, \
                make_response
from io import StringIO
import csv

from models.Item import Item
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import datetime
from db import db

# POST /item/create
def create():
    # data = request.json
    data = request.form
    print(data)
    item = Item(
        name = data.get("name", ""),
        type = data.get("type", ""),
        stock = data.get("stock", 0),
        description = data.get("description", ""),
        date = datetime.datetime.now()
    )
    db.session.add(item)
    db.session.commit()
    # return f"Successfully created item {item.id}"
    return redirect(url_for("home"))

# DELETE /item/delete
# Delete an item by id
def delete(itemId):
    item = Item.query.get_or_404(itemId)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))

# PATCH /item/update
# Update an item by id
def update(itemId):
    print("REQ IS", request)
    data = request.form
    print("dat is", data)
    item = Item.query.get_or_404(itemId)
    for key in data.keys():
        setattr(item, key, data[key] if key in data else getattr(item, key))
    db.session.commit()
    return redirect(url_for('home'))

# GET /item/list
# List all items
# Response is an array of json serialized rows
def list():
    result = Item.query.order_by(Item.date).all()
    resultJson = [x.serialize for x in result]
    return jsonify(resultJson)

# Extra feature:
# GET /item/export
# Export the table as a csv
def export():
    io = StringIO()
    cw = csv.writer(io)
    query = Item.query.order_by(Item.date).all()

    # Write the column names
    cw.writerow([x for x in query[0].serialize.keys()])

    for book in query:
        "dat is"
        cw.writerow([str(x) for x in book.serialize.values()])
    #     cw.writerows(str(x) for x in book.serialize.values())
    output = make_response(io.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output
