from flask import Blueprint ,render_template

auth = Blueprint('auth', __name__)

@auth.route('/Login')
def login():
   
    return render_template("login.html")

@auth.route('/Logout')
def logout():
    return "<p>Logout</p>"  

@auth.route('/sign-up')
def sign_up():
   
    return render_template("signup.html")