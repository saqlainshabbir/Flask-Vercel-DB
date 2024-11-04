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

# New schema for storing Electrical Stores Data details
class Electrical_stores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Sports Shops Data details
class Sports_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Car wash Data details
class Car_washses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Car Dealers Data details
class Car_dealers(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Bike Dealers Data details
class Bike_dealers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Car Work Shops Data details
class Car_work_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Tractors Dealers Data details
class Tractors_dealers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(120), nullable=True)
    location = db.Column(db.String(120), nullable=True)
    user_type = db.Column(db.String(50), nullable=False)  # e.g., Dealer, Individual
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    vehicle_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    transmission = db.Column(db.String(50), nullable=False)  # e.g., Automatic, Manual
    fuel_type = db.Column(db.String(50), nullable=False)  # e.g., Petrol, Diesel
    engine_capacity = db.Column(db.Integer, nullable=True)
    location = db.Column(db.String(120), nullable=True)
    image_file = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Books Center Data details
class Book_centers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Travelling Agencies Data details
class Travelling_agencies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Beauty Parlours Data details
class Beauty_parlours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Building Materials Data details
class Building_materials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Gift and Toys Shops Data details
class Gift_and_toys_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Bakeries Data details
class Bakeries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Swimming Pools Data details
class Swimming_pools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Cement Shops Data details
class Cement_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Gynaecologists Data details
class Gynaecologists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Laboratories Data details
class Laboratories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Computers Data details
class Computers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Mobile Shops Data details
class Mobile_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Gyms Data details
class Gyms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Clinics Data details
class Clinics(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Printing Shops Data details
class Printing_shops(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing taylors shops Data details
class Taylors_shops(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing marbles shops Data details
class Marbles_shops(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Pest Controls Data details
class Pest_controls(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Academies Data details
class Academies(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Dairy Farms Data details
class Dairy_farms(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing shoe stores Data details
class Shoes_stores(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Private Colleges Data details
class Private_colleges(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Private Schools Data details
class Private_schools(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing Private Hospitals Data details
class Private_hospitals(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# New schema for storing orthopedic hospitals Data details
class Orthopedic_hospitals(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    tehsil = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)