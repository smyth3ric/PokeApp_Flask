
from app import app
from flask import render_template



@app.route('/') 
def homePage():
    return render_template('index.html')



@app.route('/test') 
def test():
    return render_template('test.html')