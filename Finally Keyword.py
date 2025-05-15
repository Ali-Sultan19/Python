# In function we can run all the commands like try except and finally
def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed") if we can write a print statement whereas finally then it cant run in function


x = func1()
print(x)