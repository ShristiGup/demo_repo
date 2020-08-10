import sqlite3
school=sqlite3.connect("schooltest.db")
nm = input("Enter name:")
sql = "SELECT * FROM STUDENTS WHERE NAME='"+nm+"';"
cur = school.cursor()
cur.execute(sql)
record = cur.fetchone()
print(record)
if record!=None:
    res = input("Do you want to delete this record? (Y/N)")
    sql = "DELETE FROM STUDENTS WHERE NAME='"+nm+"';"
    if res=="Y":
        try:
            cur.execute(sql)
            school.commit()
            print("RECORD DELETED SUCCESSFULLY")
        except:
            print("ERROR OCCURRED")
            school.rollback()
school.close()
