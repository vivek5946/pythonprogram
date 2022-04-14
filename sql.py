import sqlite3

# this is useful to data add single data at one time


def insertdata(id, name, marks):
    con = sqlite3.connect("student.db")
    cursor = con.cursor()

    # parameterized query
    insert_query = '''INSERT INTO stud_marks VALUES(?,?,?)'''
    cursor.execute(insert_query, (id, name, marks))
    con.commit()
    con.close()


a = int(input('enter the student id:'))
b = input('enter the student name:')
c = int(input('enter the student marks:'))


insertdata(a, b, c)
#insertdata(3, 'jan', 90)
# ---------------This is useful to add multiple data at single point------


def insertmultipledata(datalist):
    con = sqlite3.connect("student.db")
    cursor = con.cursor()

    # parameterized query
    insert_query = '''INSERT INTO stud_marks VALUES(?,?,?)'''
    cursor.executemany(insert_query, datalist)
    con.commit()
    print('Total records inserted:', cursor.rowcount)
    con.commit()
    con.close()


datalist = [(20, 'raju', 90), (30, 'ajinkya', 100), (67, 'gaurav', 90)]
insertmultipledata(datalist)
