import DbConnection.conn

db = DbConnection.conn

#update one row
db.myCursor.execute("UPDATE tbl_person SET person_last_name = 'Shubham' WHERE person_id = 2")

db.myDb.commit()
print(db.myCursor.rowcount, "record affected")

