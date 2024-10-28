from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Subscription, Newsletter
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

@app.route('/newsletter', methods=['POST'])
def add_newsletter():
    title = request.form['title']
    content = request.form['content']
    new_newsletter = Newsletter(title=title, content=content)
    db.session.add(new_newsletter)
    db.session.commit()
    flash('Newsletter created successfully!', 'success')
    return redirect(url_for('index'))