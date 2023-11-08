from flask import Flask, render_template, request, redirect, url_for
from admin_dashboard import add_staff_to_database
from flask import render_template, request
from admin_dashboard import add_staff_to_database, get_staff_details

import mysql.connector

app = Flask(__name__)

# Establish connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deandofe#2023",
    database="software"
)

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM admin_table WHERE username = %s AND password = %s", (username, password))
        admin = mycursor.fetchone()

        if admin:
            return redirect(url_for('admin_dashboard'))
        else:
            return "Error: Invalid credentials"

    return render_template('admin_login.html')


@app.route('/admin_dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        domain = request.form['domain']  # Retrieve the 'domain' value from the form
        add_staff_to_database(username, password, domain)  # Pass the 'domain' value to the function

    staff_details = get_staff_details()
    return render_template('admin_dashboard.html', staff_details=staff_details)


@app.route('/staff_login', methods=['GET', 'POST'])
def staff_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM staff_table WHERE username = %s AND password = %s", (username, password))
        staff = mycursor.fetchone()

        if staff:
            return redirect(url_for('staff_dashboard'))
        else:
            return "Error: Invalid credentials"

    return render_template('staff_login.html')

@app.route('/staff_dashboard', methods=['GET', 'POST'])
def staff_dashboard():
    if request.method == 'GET':
        return render_template('staff_dashboard.html', domain="fruits")  # Pass the domain name as required

    # Logic for updating the unit_remaining for each fruit
    if request.method == 'POST':
        fruit_name = request.form['fruit_name']
        updated_units = request.form['updated_units']

        # Add your logic here to update the 'fruits' table based on the submitted form data
        mycursor = mydb.cursor()
        update_query = "UPDATE fruits SET unit_remaining = %s WHERE fruit_name = %s"
        mycursor.execute(update_query, (updated_units, fruit_name))
        mydb.commit()
        mycursor.close()
        print(f"Fruit Name: {fruit_name}, Updated Units: {updated_units}")

        return redirect(url_for('staff_dashboard'))  # Redirect back to the staff dashboard after updating the units

    return render_template('staff_dashboard.html', domain="fruits")  # Pass the domain name as required

if __name__ == '__main__':
    app.run(debug=True)
