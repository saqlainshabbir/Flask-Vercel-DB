from datetime import datetime
from app import db

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    father_name = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(120), nullable=True)
    subscribed_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing newsletter details
class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)