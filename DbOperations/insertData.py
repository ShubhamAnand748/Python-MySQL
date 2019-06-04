import DbConnection.conn

db = DbConnection.conn

#insert one row
db.myCursor.execute("INSERT INTO tbl_person (person_first_name, person_last_name, person_age) VALUES ('Shubham', 'Anand', '22')")
try:
    print(db.myCursor.rowcount, 'row inserted.')
except:
    print('Error')


#insert multiple rows
db.myCursor.execute("INSERT INTO tbl_person (person_first_name, person_last_name, person_age) VALUES ('Anand', 'Shubham', '22'), ('Shubham', '', '22'), ('Anand', '', '22')")
try:
    print(db.myCursor.rowcount, 'rows inserted.')
except:
    print('Error')

db.myDb.commit()