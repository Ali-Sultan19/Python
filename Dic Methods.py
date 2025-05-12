# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Original Dictionary:", my_dict)

# 1. get() - safely access a key
print("\nget('name'):", my_dict.get("name"))
print("get('gender', 'Not Found'):", my_dict.get("gender", "Not Found"))

# 2. keys() - get all keys
print("\nKeys:", list(my_dict.keys()))

# 3. values() - get all values
print("Values:", list(my_dict.values()))

# 4. items() - get all key-value pairs
print("Items:", list(my_dict.items()))

# 5. update() - merge another dictionary
my_dict.update({"age": 26, "gender": "Female"})
print("\nAfter update():", my_dict)

# 6. pop() - remove key and return its value
age = my_dict.pop("age")
print("\nAfter pop('age'):", my_dict)
print("Popped age:", age)

# 7. popitem() - remove last inserted item
last_item = my_dict.popitem()
print("\nAfter popitem():", my_dict)
print("Popped item:", last_item)

# 8. setdefault() - get value if key exists, else set default
hobby = my_dict.setdefault("hobby", "Reading")
print("\nAfter setdefault('hobby', 'Reading'):", my_dict)
print("Returned hobby:", hobby)

# 9. copy() - make a shallow copy of dictionary
copied_dict = my_dict.copy()
print("\nCopied Dictionary:", copied_dict)

# 10. clear() - remove all items
my_dict.clear()
print("\nAfter clear():", my_dict)
