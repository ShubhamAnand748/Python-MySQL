import DbConnection.conn

db = DbConnection.conn

#delete one row
db.myCursor.execute("DELETE FROM tbl_person WHERE person_id = 2")

db.myDb.commit()
print(db.myCursor.rowcount, "record affected")
