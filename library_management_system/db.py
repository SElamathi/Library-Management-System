import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Elamathi@2005",
        database="library_management_system"  # UPDATED NAME
    )
