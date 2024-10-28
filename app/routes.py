from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Subscription, Solar_shops, Karyana_shops, Real_estates, Bird_shops, fast_foods, Housing_schemes, Madaris, Agriculture_shops
from sqlalchemy.exc import IntegrityError

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