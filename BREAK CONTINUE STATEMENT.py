for i in range(12):
    i = i + 1
    if (i == 11):
        break
    print("5 X", i, "=", 5 * i)

i = 0
while True:
    print(i)
    i = i + 1
    if (i % 13 == 0):
        break

for i in range(1, 10, 1):
    print(i, end="  ")
    if (i == 7):
        break
    else:
        print("Mississippi")
print("Thank you")