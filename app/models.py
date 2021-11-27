from app import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    legacy_id = db.Column(db.String())
    description = db.Column(db.String())
    name = db.Column(db.String())
    price = db.Column(db.String())
    seller = db.Column(db.String())
    url = db.Column(db.String())
    agent_id = db.Column(db.Integer)
    image_url = db.Column(db.String())

    def __init__(self, legacy_id, description, name, price,seller, url):
        self.url = url
        self.legacy_id = legacy_id
        self.description = description
        self.name=name
        self.price=price
        self.seller=seller
    

    def __repr__(self):
        return '<id {}>'.format(self.id)