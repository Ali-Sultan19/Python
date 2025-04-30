# Declair a set
print('Sets is a well defined objects')
sett = {1,2,3,4,5,6}
print(type(sett)) # type of data
print(sett)


x ={1,2,2,3,3,4,5,6,6,7,7,7} # no repetition occur in sets
print(x)


sets = {1,'ali',2,'manahil',3,'nomi'}    # is sets the value are not fix
for x in sets:
    print(x)

s = {}   #  in this use empty set can define a dictionary
print(type(s))



st=set() # use use to declain a empty set by using set functon
print(type(st))



# Create a set
my_set = {1, 2, 3, 4, 5}


# Check membership
if 2 in my_set:
    print("2 is in the set")

# Iterate over a set
for item in my_set:
    print(item)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a | set_b)        # {1, 2, 3, 4, 5}
print("Intersection:", set_a & set_b) # {3}
print("Difference:", set_a - set_b)   # {1, 2}