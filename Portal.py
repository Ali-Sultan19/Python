a = int(input("Enter your Roll number : "))
print(a)


if(a==1):
    print("Your name is Ali")
    print("You are a BSCS student")
    print("Your father name is Farman Ali")

    b = int(input("Enter your marks : "))
    print(b)

    if(b<=20):
        print("You are to able to continue your study ")
    else:
        print("You can choose all subjects ")


elif(a==2):
    print("Your name is Komal")
    print("You are a BSCS student")
    print("Your father name is Mirza")

    b = int(input("Enter your marks : "))
    print(b)

    if (b <= 15):
        print("You are to able to continue your study ")
    else:
        print("You can choose only 3 subjects ")

elif(a==3):
    print("Your name is Farzam")
    print("You are a BSCS student")
    print("Your father name is Asad")

    b = int(input("Enter your marks : "))
    print(b)

    if (b <= 10):
        print("You are to able to continue your study ")
    else:
        print("You can choose only 2 subjects ")

elif(a==4):
    print("Your name is Nauman")
    print("You are a BSCS student")
    print("Your father name is Ali")

    b = int(input("Enter your marks : "))
    print(b)

    if (b <= 5):
        print("You are to able to continue your study ")
    else:
        print("Your marks is too low ")

elif(a==5):
    print("Your name is Manahil")
    print("You are a BSCS student")
    print("Your father name is Hanif")

    b = int(input("Enter your marks : "))
    print(b)

    if (b <= 0):
        print("You are to able to continue your study ")
    else:
        print("You are not allowed to continue your study ")

else:
    print("Please enter the number Between 1-5 :")