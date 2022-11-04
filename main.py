def size():
  print("[1] large pizza $6.00")
  print("[2] extra large pizza $10.00")
  print("[0] cancel order")

def topping():
  print("[1] 1 topping $1.00")
  print("[2] 2 toppings $1.75")
  print("[3] 3 toppings $2.50")
  print("[4] 4 toppings $3.35")
  print("[0] cancel order")
op1=True
while True:
  try:
    size()
    op1=int(input("what size do you want?\n"))
      
  except ValueError:
    print("please enter a number between 0-2")
    continue
    
  else:
    if op1 ==1:
      m=6.00
      break
    elif op1 ==2:
      m=10.00
      break
    elif op1 ==0:
      print("order cancelled")
      break
    else:
      print("please enter a number between 0-2")
    continue
op2=True
while True:
  try:
    topping()
    op2=int(input("how many toppings do you want, cheese included\n"))

  except ValueError:
    print("please enter a number between 0-4")
    continue

  else:
    if op2 == 1:
      m1=1.00
      break
    elif op2 ==2:
      m1=1.75
      break
    elif op2 ==3:
      m1=2.50
      break
    elif op2 ==4:
      m1=3.35
      break
    elif op2 ==0:
      print("order cancelled")
      break
    else:
      print("please enter a number between 0-4")
      continue
total=round((m+m1)*1.13,2)
print("the total cost of the pizza is $", total)
  