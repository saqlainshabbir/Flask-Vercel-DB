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
class Agriculture_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Solar details
class Solar_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Karyana Shops details
class Karyana_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Karyana Shops details
class Real_estates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Birds Shops details
class Bird_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing fast foods details
class fast_foods(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing housing schemes details
class Housing_schemes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Madaris details
class Madaris(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Hotels data details
class Hotels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Lodhran Profile details
class Lodhran_profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    discription = db.Column(db.String(200), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Marriage Halls Data details
class Marriage_halls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Union Councils of Dunyapur details
class Union_councils(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Union_council_name = db.Column(db.String(100), nullable=False)
    Union_council_discription = db.Column(db.String(200), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Lawyers Data details
class Lawyers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing furniture Shops Data details
class Furniture_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Software Houses Data details
class Software_houses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Dentals Data details
class Dentals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Electronics Shops Data details
class Electronics_shops(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)