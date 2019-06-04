import DbConnection.conn

db = DbConnection.conn

db.myCursor.execute("SELECT * FROM tbl_person LIMIT 2")
result = db.myCursor.fetchall()
for data in result:
    print("Person data with LIMIT 2: ", data)

db.myCursor.execute("SELECT * FROM tbl_person LIMIT 2 OFFSET 1")
result1 = db.myCursor.fetchall()
for data1 in result1:
    print("Person data with LIMIT 2 and OFFSET 1: ", data1)

db.myCursor.execute("SELECT * FROM tbl_person LIMIT 2, 1")
result2 = db.myCursor.fetchall()
for data2 in result2:
    print("Person data with LIMIT 2, 1: ", data2)
