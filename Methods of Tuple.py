t1 = (1,2,3,4,5,6,7)
t2 = (8,9,10,11,12,13,14)

#indexing
print(t1[6]) #indexing
print(t2[0])

#concentation
t= t1+t2  # joining the tuple
print(t)

# reptition
print(t1*2) #each tuple multiply
print(t2*4)

# check
print(3 in t1) # check the element in tuples
print(6 in t1)
print(16 in t2)

# iteration
for i in t1:
    print('Im Aliy') # no of elements in tuples


# lenght
print(len(t1)) # no of elements in tuple
print(len(t2))

# min max sum
print(min(t1)) #min
print(max(t1)) #max
print(sum(t1)) #sum
print(min(t2))
print(max(t2))
print(sum(t2))

#nested tuple
Tuple =(1,(2,3,4,5))
print(Tuple)

#variable assign
a,b =(1,2)
print(a,b)