from flask_sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    passhash = db.Column(db.String(512), nullable=False)
    name = db.Column(db.String(64), nullable=False)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Float, nullable=False)
    man_date = db.Column(db.Date, nullable=False)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'category.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    # relationships
    profucts = db.relationship('Product', backref='category', lazy=True)
    # we define this relation ship so that if we do product.category we get that object and also if we use .product in categories class we get a list of products in that category
    # lazy is kept true to make sure its loaded only if we call it or we require it


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
