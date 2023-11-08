import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Deandofe#2023",
    database="software"
)

def add_staff_to_database(username, password, domain):
    mycursor = mydb.cursor()
    try:
        mycursor.execute("INSERT INTO staff_table (username, password, domain) VALUES (%s, %s, %s)", (username, password, domain))
        mydb.commit()
        print(f"Staff with username {username} added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mycursor.close()



def get_staff_details():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM staff_table")
    staff_details = mycursor.fetchall()
    mycursor.close()
    return staff_details
