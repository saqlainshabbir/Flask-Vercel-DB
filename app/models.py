from datetime import datetime
from app import db

# class Subscription(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     name = db.Column(db.String(120), nullable=False)
#     father_name = db.Column(db.String(120), nullable=False)
#     phone_number = db.Column(db.String(120), nullable=True)
#     subscribed_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing newsletter details
class Agriculture_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)