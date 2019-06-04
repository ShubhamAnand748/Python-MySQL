import DbConnection.conn

db = DbConnection.conn

#create database
db.myCursor.execute("CREATE DATABASE testPython")

try:
    print('Database created successfully.')
except:
    print('Unable to create the database.')