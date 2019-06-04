import  DbConnection.conn
db =  DbConnection.conn

db.myCursor.execute("SELECT * FROM tbl_person HAVING person_age IN (22, 13, 19)")
result =  db.myCursor.fetchall()
for data in result:
    print(data)