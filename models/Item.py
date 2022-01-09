from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
import uuid

from db import db 

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(256), nullable = False)
    type = db.Column(db.String(256), nullable = False)
    stock = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(256), nullable = False)
    date = db.Column(db.DateTime(), nullable= False)

    def __repr__(self):
        return f"<Item {self.name}"

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'stock': self.stock,
            'description': self.description,
            'date': self.date
        }
