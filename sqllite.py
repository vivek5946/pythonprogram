
import sqlite3
con = sqlite3.connect("student.db")
cursor = con.cursor()
sqlite_query = '''CREATE TABLE stud_marks( id INTEGER PRIMARY KEY,name TEXT NOT NULL,marks INTEGER NOT NULL);'''
cursor.execute(sqlite_query)
print("table is created succesfully")

sqlite_insert_query = '''INSERT INTO stud_marks VALUES(1001,'tom',95)'''
cursor.execute(sqlite_insert_query)
print("a student record is inserted")
con.commit()
con.close()
