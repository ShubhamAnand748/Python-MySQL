import DbConnection.conn

db = DbConnection.conn

#select all order by
db.myCursor.execute("SELECT * FROM tbl_person ORDER BY person_id ASC")
result = db.myCursor.fetchall()
for data in result:
    print(data)

