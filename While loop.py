i = int(input("Enter the number: "))
print(i)
while(i<=5):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")

count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")


x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

x = 1
while (x < 5):
    print(x)
    x = x + 1
else:
    print('counter is 0')

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    print("That's not a positive number.")
    break