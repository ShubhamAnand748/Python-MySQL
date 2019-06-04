import DbConnection.conn

db = DbConnection.conn

#create table
db.myCursor.execute("CREATE TABLE tbl_person (person_id int NOT NULL AUTO_INCREMENT, person_first_name varchar(255) NOT NULL, person_last_name varchar(255), person_age int, PRIMARY KEY (person_id))")

try:
    print('Table created successfully.')
except:
    print('Unable to create table.')