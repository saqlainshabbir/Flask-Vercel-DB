from flask import render_template, request, redirect, url_for, flash
from app import app, db
import os
from app.models import (
    Subscription, Solar_shops, Karyana_shops, Real_estates, Bird_shops, 
    fast_foods, Housing_schemes, Madaris, Hotels, Lodhran_profile, 
    Marriage_halls, Union_councils, Lawyers, Furniture_shops, Clinics,
    Software_houses, Dentals, Electronics_shops, Electrical_stores, Dairy_farms,
    Sports_shops, Car_washses, Car_dealers, Bike_dealers, Gyms,  Taylors_shops,
    Car_work_shops, Tractors_dealers, Vehicles, User, Book_centers, Printing_shops,
    Travelling_agencies, Beauty_parlours, Building_materials, Agriculture_shops,
    Gift_and_toys_shops, Bakeries, Swimming_pools, Cement_shops, Gynaecologists,
    Laboratories, Computers, Mobile_shops, Marbles_shops, Pest_controls, Academies,
    Shoes_stores, Private_colleges, Private_schools, Private_hospitals, Orthopedic_hospitals
)
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
from flask import send_from_directory

# Set the folder to save images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    name = request.form['name']
    father_name = request.form['father_name']
    phone_number = request.form['phone_number']
    new_subscription = Subscription(email=email, name=name, father_name=father_name, phone_number=phone_number)
    try:
        db.session.add(new_subscription)
        db.session.commit()
        flash('Subscription successful!!', 'success')
    except IntegrityError:
        db.session.rollback()
        flash('This email is already subscribed.', 'error')
    return redirect(url_for('index'))

@app.route('/Agriculture_shops', methods=['POST'])
def Agriculture_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Agriculture_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Newsletter created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Solar_shops', methods=['POST'])
def Solar_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Solar_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Newsletter created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Karyana_shops', methods=['POST'])
def Karyana_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Karyana_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Newsletter created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Real_estates', methods=['POST'])
def Real_estate():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Real_estates(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Newsletter created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Bird_shops', methods=['POST'])
def Bird_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Bird_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Birds shop created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/fast_foods', methods=['POST'])
def Fast_food():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = fast_foods(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Fast Foods Shop created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Housing_schemes', methods=['POST'])
def Housing_scheme():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Housing_schemes(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Housing scheme Shop created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Madaris', methods=['POST'])
def Madares():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Madaris(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Madaris created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Hotels', methods=['POST'])
def Hotel():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Hotels(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Hotels created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Lodhran_profile', methods=['POST'])
def Lodhran_Profile():
    name = request.form['name']
    discription = request.form['discription']
    new_newsletter = Lodhran_profile(name=name, discription=discription)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Lodhran Profile created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Marriage_halls', methods=['POST'])
def Marriage_hall():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Marriage_halls(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Marriage halls created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Union_councils', methods=['POST'])
def Union_council():
    Union_council_name = request.form['Union_council_name']
    Union_council_discription = request.form['Union_council_discription']
    new_newsletter = Union_councils(Union_council_name=Union_council_name, Union_council_discription=Union_council_discription)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Union Councils created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Lawyers', methods=['POST'])
def Lawyer():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Lawyers(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Lawyers data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Furniture_shops', methods=['POST'])
def Furniture_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Furniture_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Furniture Shops data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Software_houses', methods=['POST'])
def Software_house():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Software_houses(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Software Houses data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Dentals', methods=['POST'])
def Dental():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Dentals(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Dentals data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Electronics_shops', methods=['POST'])
def Electronics_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Electronics_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Electronics Shops data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Electrical_stores', methods=['POST'])
def Electrical_store():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Electrical_stores(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Electrical Stores data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Sports_shops', methods=['POST'])
def Sports_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Sports_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Sports Shops data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Car_washses', methods=['POST'])
def Car_wash():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Car_washses(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Car wash data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Car_dealers', methods=['POST'])
def Car_dealer():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Car_dealers(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Car Dealers data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Bike_dealers', methods=['POST'])
def Bike_dealer():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Bike_dealers(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Car Dealers data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Car_work_shops', methods=['POST'])
def Car_work_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Car_work_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Car Work Shops data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Tractors_dealers', methods=['POST'])
def Tractors_dealer():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Tractors_dealers(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Tractors Dealers data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/User', methods=['POST'])
def Users():
    name = request.form['name']
    email = request.form['email']
    password_hash = request.form['password_hash']
    phone_number = request.form['phone_number']
    location = request.form['location']
    user_type = request.form['user_type']
    new_user = User(name=name, email=email, password_hash=password_hash, phone_number=phone_number, location=location, user_type=user_type)
    db.session.add(new_user)
    db.session.commit()
    flash('New User Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/Vehicles', methods=['POST'])
def Vehicle():
    title = request.form['title']
    price = request.form['price']
    year = request.form['year']
    mileage = request.form['mileage']
    transmission = request.form['transmission']
    fuel_type = request.form['fuel_type']
    engine_capacity = request.form['engine_capacity']
    location = request.form['location']
     # Handle image file upload
    image_file = request.files['image_file']
    image_url = None
    if image_file:
        filename = secure_filename(image_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(file_path)
        image_url = url_for('uploaded_file', filename=filename, _external=True)
    new_vehicle = Vehicles(title=title, price=price, year=year, mileage=mileage, transmission=transmission,fuel_type=fuel_type, engine_capacity=engine_capacity, location=location, image_file=image_url)
    db.session.add(new_vehicle)
    db.session.commit()
    flash('Vehicles data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicles.query.all()
    return render_template('vehicles.html', vehicles=vehicles)

@app.route('/Book_centers', methods=['POST'])
def Book_center():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Book_centers(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Tractors Dealers data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Travelling_agencies', methods=['POST'])
def Travelling_agencie():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Travelling_agencies(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Travelling Agencies data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Beauty_parlours', methods=['POST'])
def Beauty_parlour():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Beauty_parlours(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Travelling Agencies data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Building_materials', methods=['POST'])
def Building_material():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Building_materials(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Travelling Agencies data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Gift_and_toys_shops', methods=['POST'])
def Gift_and_toys_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Gift_and_toys_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Gift and Toys Shops data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Bakeries', methods=['POST'])
def Bakerie():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Bakeries(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Gift and Toys Shops data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Swimming_pools', methods=['POST'])
def Swimming_pool():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Swimming_pools(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Swimming Pools data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Cement_shops', methods=['POST'])
def Cement_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Cement_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Cement Shops data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Gynaecologists', methods=['POST'])
def Gynaecologist():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Gynaecologists(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Gynaecologists data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Laboratories', methods=['POST'])
def Laboratorie():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Laboratories(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Laboratories data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Computers', methods=['POST'])
def Computer():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Computers(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Computers data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Mobile_shops', methods=['POST'])
def Mobile_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Mobile_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Mobile Shops data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Gyms', methods=['POST'])
def Gym():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Gyms(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Gyms data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Clinics', methods=['POST'])
def Clinic():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Clinics(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Clinics data Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Printing_shops', methods=['POST'])
def Printing_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Printing_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Printing Shop Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Taylors_shops', methods=['POST'])
def Taylors_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Taylors_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Taylor Shop Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Marbles_shops', methods=['POST'])
def Marbles_shop():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Marbles_shops(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Marbles Shop Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Pest_controls', methods=['POST'])
def Pest_control():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Pest_controls(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Pest Control Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Academies', methods=['POST'])
def Academie():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Academies(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Academy Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Dairy_farms', methods=['POST'])
def Dairy_farm():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Dairy_farms(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Dairy Farm Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Shoes_stores', methods=['POST'])
def Shoes_store():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Shoes_stores(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Shoes Store Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Private_colleges', methods=['POST'])
def Private_college():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Private_colleges(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Private College Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Private_schools', methods=['POST'])
def Private_school():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Private_schools(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Private School Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Private_hospitals', methods=['POST'])
def Private_hospital():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Private_hospitals(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Private Hospital Added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/Orthopedic_hospitals', methods=['POST'])
def Orthopedic_hospital():
    name = request.form['name']
    phone_number = request.form['phone_number']
    district = request.form['district']
    tehsil = request.form['tehsil']
    address = request.form['address']
    town = request.form['town']
    new_newsletter = Orthopedic_hospitals(name=name, phone_number=phone_number, district=district, tehsil=tehsil, address=address, town=town)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Orthopedic Hospital Added successfully!', 'success')
    return redirect(url_for('index'))