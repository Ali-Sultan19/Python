#Create List
List = [1,2,3,4]
print (List)

print('slicing')
Colors = ['red','orange','yellow','blue','green','purple']
print(Colors[0])
print(Colors[4])

#Slicing
print(Colors[0:])
print(Colors[:3])
print(Colors[1:4])
print(Colors[-4:-1])


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
#Slicing
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes

print(animals[-4])
print(animals[len(animals)-4])
print(animals[5])



animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
#using range
print('range')
print(animals[1:8:3])
print(animals[0:8:2])


#also create a list using list comprehension method
list=[i for i in range(5)]
print(list)
list=[i*i for i in range(10) if i%2==0]
print(list)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item] # o present in name
print(namesWith_O)
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)] #range or elements more than four in names
print(namesWith_O)

#condition
if 'pig' in animals:
    print('yes')
else:
    print('no')
