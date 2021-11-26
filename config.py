import os
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://szlikxxxsncvyh:76df9a0905ef0ef2170da0ac7d9d5889c62f2e83d124f7b37febe03dda5cc376@ec2-54-228-209-117.eu-west-1.compute.amazonaws.com:5432/d2j7i18j7mu6q4'
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    legacy_id = db.Column(db.String())
    description =db.Column(db.String())
    name = db.Column(db.String())
    price = db.Column(db.String())
    seller = db.Column(db.String())
    url = db.Column(db.String())
    agent_id = db.column(db.Integer)

    def __init__(self, legacy_id, description, name, price,seller, url):
        self.url = url
        self.legacy_id = legacy_id
        self.description = description
        self.name=name
        self.price=price
        self.seller=seller
    

    def __repr__(self):
        return '<id {}>'.format(self.id)
