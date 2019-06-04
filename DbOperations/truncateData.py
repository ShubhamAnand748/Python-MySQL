import DbConnection.conn

db = DbConnection.conn

#delete all rows or truncate table
db.myCursor.execute("TRUNCATE TABLE tbl_person")

try:
    print("Truncate successfully.")
except:
    print("Data can't be delete from table.")

