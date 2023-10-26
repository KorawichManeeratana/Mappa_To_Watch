from flask import Blueprint, render_template, request, flash
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username =  request.form.get('username')
        password = request.form.get('password')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 3 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
            
    return render_template("")
