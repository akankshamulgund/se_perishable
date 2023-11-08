import mysql.connector

# Establish connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deandofe#2023",
    database="software"
)

# Create fruits table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS fruits (id INT AUTO_INCREMENT PRIMARY KEY, fruit_name VARCHAR(255), unit_loaded INT, unit_remaining INT)")

# Close the cursor and connection
mycursor.close()
mydb.close()
