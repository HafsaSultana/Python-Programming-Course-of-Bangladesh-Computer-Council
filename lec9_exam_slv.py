# 1
day_num = int(input("Enter a number (1-7): "))
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid number. Please enter a number between 1 and 7.")



# 2

def love6(a, b):
  sum_ab=a+b
  sub_ab=abs(a-b)
  if sum_ab==6 or sub_ab==6 or a==6 or b==6:
    return True
  else:
    return False

#3
def diff21(n):
  if n<=21:
    difference = 21-n
  else:
    difference =2*(n-21)
  return difference 
    

