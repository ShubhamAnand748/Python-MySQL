import DbConnection.conn

db = DbConnection.conn

#select all
db.myCursor.execute("SELECT * FROM tbl_person")
result = db.myCursor.fetchall()
for data in result:
    print(data)

