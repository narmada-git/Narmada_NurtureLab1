from flask import render_template, flash, redirect, url_for, request
from nuturelab.forms import RegistrationForm, LoginForm, DetailsForm
from nuturelab import app, db
from nuturelab.models import Employees




@app.route("/")
@app.route("/admin")
def Admin():
    return render_template('admin.html', title='Admin')


@app.route('/add', methods=['GET', 'POST'])
def addEmployee():
    if request.method == 'POST':
        if not request.form['user_id'] or not request.form['username']:
            flash('Please enter all the fields', 'error')
        else:
            employee = Employees(request.form['user_id'], request.form['username'],
                                 request.form['photo_url'])

            db.session.add(employee)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('advisor_result'))
    return render_template('admin.html')


@app.route('/advisor', methods=['POST', 'GET'])
def advisor():
    if request.method == 'POST':
        result = request.form
        return render_template("advisor_result.html", result=result)


@app.route("/User")
def User():
    return render_template('user.html', title='User')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('User'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have been logged in!', 'success')
        return redirect(url_for('User'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/details")
# @app.route("/user/<user-id>/advisor")
def details():
    form = DetailsForm()
    if form.validate_on_submit():
        flash(f'200_OK if the request is successful')
        return redirect(url_for('advisor'))


@app.route("/user/<user_id>/advisor", methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        result = request.form
        return render_template("advisor_result.html", result=result)

