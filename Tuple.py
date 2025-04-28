#using tuple
tuple = (1,)
print(type,tuple)
t = (1,2,3,4,5,6,7,8,9,0)
print(t)


tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

t1 = tuple1[:]
t2 = tuple1[1:]
t3 = tuple1[:5]
t4 = tuple2[0:2]
t5 = tuple1[1:5]
t6 = tuple1[-5:-3]
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)


country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])


country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country: # check the element in tuple
    print("Germany is present.")
else:
    print("Germany is absent.")


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3]) # range 