
from app import app
from flask import render_template



@app.route('/') 
def homePage():
    return render_template('home.html')



@app.route('/favorite5') 
def favorite5():
    return render_template('favorite5.html')