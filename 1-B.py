def factorial(n):
  f=1
  if n == 0:
      return 1
  else:
    while n>0:
      f=f*n
      n-=1
        
    return f
while True:
  num = int(input("أدخل عددًا لحساب المضروب: "))
  print(f"مضروب {num} هو {factorial(num)}")
  s=input("Do you want to continue, y or n").lower()
  if s=="n":
    break
