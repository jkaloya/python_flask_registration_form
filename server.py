from flask import Flask, render_template, session, redirect, request, flash
import re
from datetime import datetime, date, time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def regist():
    print "Got Post Info"
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']

    valid = True
    if not request.form['first_name'].isalpha():
        flash("First name cannot be empty!", "error")
        valid = False

    if not request.form['last_name'].isalpha():
        flash("Last name cannot be empty or have numbers!", "error")
        valid = False

    if len(request.form['email']) < 1:
        flash("Email cannot be empty!", "error")
        valid = False

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "error")
        valid = False

    if not request.form['birth_date'].isalpha():
        flash("Birth date cannot be empty!", "error")
        valid = False

    if len(request.form['password']) <= 8:
        flash("Password must be more than 8 characters!", "error")
        valid = False

    elif not passwordRegex.match(request.form['password']):
        flash("Password must contain at least one lowercase letter, one uppercase letter, and one digit", "error")

    if request.form['password'] != request.form['confirm_password']:
        flash("Password and confirmation password do not match!", "error")
        valid = False

    if valid:
        return redirect('/result')

    return redirect('/')

@app.route('/result')
def result():
    return render_template('result.html')

app.run(debug=True)
