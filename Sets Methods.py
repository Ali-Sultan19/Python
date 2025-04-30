#   union and update of sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)                      # There are different methods to take union
cities.update(cities2)
print(cities)
print("Union : " , cities | cities2)


#    using intersection and intersection_update

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)                      # There are different methods to take intersection
cities.intersection_update(cities2)
print(cities)
print('Intersection : ' , cities & cities2)




#    using symmetric_difference and symmetric_difference_update

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)                      # There are different methods to take Symmetric_difference
cities.symmetric_difference_update(cities2)
print(cities)

cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
Symmetric_difference=  cities4 ^ cities5
print('Symmetric_difference : ' ,Symmetric_difference )




#  using difference and difference_update
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
print(cities3)                      # There are different methods to take Difference
cities.difference_update(cities2)
print(cities)

cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
difference=  cities4 - cities5
print('Difference : ' , difference )




# Define sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. add()
a.add(10)
print("Add an Element in sets : " , a)
# 2. clear()
temp = a.copy()
print("Copy an Element in sets : " , temp)
temp.clear()
print("Clear an Element in sets : " , temp)

# 3. copy()
copy_a = a.copy()
print("Again copy an Element in sets : " , copy_a)

# 4. difference()
print("Difference:", a.difference(b))  # {1, 2, 10}

# 5. difference_update()
a2 = a.copy()
a2.difference_update(b)
print("After difference_update:", a2)

# 6. discard()
a.discard(10)
print("Discard 10 in sets : " , a)

# 7. intersection()
print("Intersection:", a.intersection(b))  # {3, 4}

# 8. intersection_update()
a3 = a.copy()
a3.intersection_update(b)
print("After intersection_update:", a3)

# 9. isdisjoint()
a = {1, 2, 3, 4}
b = {5, 8, 7, 6}
print("Is disjoint:", a.isdisjoint(b))  # True if no common elements

# 10. issubset()
a = {1, 2, 3, 4}
b = {3, 4,}
print("Is subset:", b.issubset(a))  # True

# 11. issuperset()
a = {1, 2, 3}
b = {1,2,3,4,}
print("Is superset:", a.issuperset(b))  # True
print("Is superset:", b.issuperset(a))  # True

# 12. pop()
val = a.pop()
print("Popped value:", val)
print("Popped value:", val+1)

# 13. remove()
a.remove(2)  # Raises KeyError if 2 not in set

# 14. symmetric_difference()
print("Symmetric difference:", a.symmetric_difference(b))  # Unique to each

# 15. symmetric_difference_update()
a4 = a.copy()
a4.symmetric_difference_update(b)
print("After symmetric_difference_update:", a4)

# 16. union()
print("Union:", a.union(b))  # Combines all

# 17. update()
a5 = {1, 2}
a5.update(b)
print("After update:", a5)
