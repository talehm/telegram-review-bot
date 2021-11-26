from app import db
from sqlalchemy.dialects.postgresql import JSON


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    legacy_id = db.Column(db.String())
    description =db.Column(db.String())
    name = db.Column(db.String())
    price = db.Column(db.String())
    seller = db.Column(db.String())
    link = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)