import math

def main():
  print("The program has begin its execution...")
  print("Your data is checked.")

def check_data(min_val,max_val):
  if min_val<10:
    print("The minimum value is:",min_val)
  if max_val>40:
    print("The maximum value is:",max_val)

def check_executed():
  return check_data(7,90)

def sq_rt(n):
  return math.sqrt(n)
  
def abs_val(n):
  return abs(n)

main()
check_executed()
print(sq_rt(64))
print(abs_val(-95.78))


