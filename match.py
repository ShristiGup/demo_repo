import sqlite3
Mydb = sqlite3.connect('FantasyCricket.db')
cur = Mydb.cursor()
sql="CREATE TABLE stats(player TEXT,matches INTEGER,runs INTEGER,'100s' INTEGER,'50s' INTEGER,value INTEGER,ctg TEXT);"
cur.execute(sql)
Mydb.close()

def main():
  print("The program has begin its execution...")
  print("Your data is checked.")
def check_data(min_val,max_val):
  if min_val<10:
    print("The minimum value is:",a)
  if max_val>40:
    print("The maximum value is:",b)

main()

