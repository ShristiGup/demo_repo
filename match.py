import sqlite3
Mydb = sqlite3.connect('FantasyCricket.db')
cur = Mydb.cursor()
sql="CREATE TABLE stats(player TEXT,matches INTEGER,runs INTEGER,'100s' INTEGER,'50s' INTEGER,value INTEGER,ctg TEXT);"
cur.execute(sql)
Mydb.close()

def main():
  print("This function will print the data generated.")
def check_data(a,b):
  if a<10:
    print("The minimum value is:",a)
  if b>40:
    print("The maximum value is:",b)
    
main()
check_data(7,90)
