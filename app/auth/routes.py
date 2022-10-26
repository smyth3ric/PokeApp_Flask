from dataclasses import dataclass
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.auth.forms import UserCreationForm
from app.auth.forms import UserLoginForm
from app.models import User 
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods=["GET", "POST"])
def signMeup():
    form= UserCreationForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            email= form.email.data
            password= form.password.data

            print(username, email, password)

            #add user to database
            user = User(username, email, password)
            #add instance to SQL
            user.saveToDB(user)

            return redirect(url_for('auth.logMeIn'))

    return render_template('signup.html', form=form)



@auth.route('/login', methods = ["GET", "POST"])
def logMeIn():
    form= UserLoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password= form.password.data

            print(username, password)

            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    print('Sucessfully logged in')
                    login_user(user)
                    return redirect(url_for('homePage'))
                else:
                    print('Incorrect password')
            else:
                print('User does not exist')

    return render_template('login.html', form=form)

@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.logMeIn'))






