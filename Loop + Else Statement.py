# Check if a number is prime using for...else
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime number")
        break
else:
    # This else runs only if the loop is *not* broken
    print(f"{number} is a prime number")

# Check if a number is prime using for...else
number = 16

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime number")
        break
else:
    # This else runs only if the loop is *not* broken
    print(f"{number} is a prime number")


for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
    if (x+1)==4:  #the condition meet the requirement then else can be ignore
        break
else:
    print ("else block in loop")
print ("Out of loop")


i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break

else:
  print("Sorry no i")

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")