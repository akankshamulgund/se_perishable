import mysql.connector

# Establish connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deandofe#2023"
)

# Drop the existing database
mycursor = mydb.cursor()
mycursor.execute("DROP DATABASE IF EXISTS software")

# Create a new database
mycursor.execute("CREATE DATABASE software")
mycursor.execute("USE software")

# Create admin_table
mycursor.execute("CREATE TABLE admin_table (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

# Insert data into admin_table
sql = "INSERT INTO admin_table (username, password) VALUES (%s, %s)"
val = ("admin", "admin")
mycursor.execute(sql, val)

# Create staff_table
mycursor.execute("CREATE TABLE staff_table (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), domain VARCHAR(255))")

# Insert data into staff_table
sql = "INSERT INTO staff_table (username, password, domain) VALUES (%s, %s, %s)"
val = [("staff1", "staff1", "fruits")]
mycursor.executemany(sql, val)

mydb.commit()
