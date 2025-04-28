def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")


def isLesser(a, b):
    pass


a = int(input('Enter a number : '))
b = int(input('Enter a number : '))
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = int(input('Enter a number : '))
d = int(input('Enter a number : '))
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
