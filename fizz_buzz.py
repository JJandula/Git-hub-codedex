


for x in range (100, 0, -1):
  if x%3 == 0 and x%5 == 0:
    print ("FizzBuzz")
  elif x % 5 == 0:
    print ("Buzz")
  elif x % 3 == 0:
    print ("Fizz")
  else:
    print(x)
