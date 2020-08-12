import sqlite3
Mydb = sqlite3.connect('FantasyCricket.db')
cur = Mydb.cursor()
sql="CREATE TABLE stats(player TEXT,matches INTEGER,runs INTEGER,'100s' INTEGER,'50s' INTEGER,value INTEGER,ctg TEXT);"
cur.execute(sql)
Mydb.close()

def main():
  pass
main()
