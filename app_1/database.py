import mysql.connector as mysql

def connection_db():
    return mysql.connect(
        user='root',
        host='localhost',
        password='5033677oki',
        database='ecole'
    )