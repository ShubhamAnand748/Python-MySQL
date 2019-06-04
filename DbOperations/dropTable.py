import DbConnection.conn

db = DbConnection.conn

#drop table
db.myCursor.execute("DROP TABLE tbl_person")

try:
    print("Table deleted successfully.")
except:
    print("Table can'nt be deleted.")
