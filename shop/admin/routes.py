from flask import render_template, session, request, redirect, url_for,flash
from shop import app,db,bcrypt
from .forms import RegistrationForm
from .modules import User
import os

#Homepage
@app.route('/')
def home():
    return "Home page"


# registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.username.data,username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form, title = "Registration page")