from datetime import datetime
from app import db

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    father_name = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(120), nullable=False)
    subscribed_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)