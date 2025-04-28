def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1,11,22,345)
print(c)


def name(**name):
    print(type(name))
    print("Hello,", name["a"], name["b"], name["c"])
name(a="James", b="Buchanan", c="Barnes")