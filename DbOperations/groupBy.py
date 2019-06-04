import DbConnection.conn

db = DbConnection.conn

#select all order by
db.myCursor.execute("SELECT COUNT(person_id), person_first_name, person_age FROM tbl_person GROUP BY person_first_name, person_age")
result = db.myCursor.fetchall()
for data in result:
    print(data)

