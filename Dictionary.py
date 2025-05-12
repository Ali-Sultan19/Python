# Creating a dictionary
student = {
    "name": "John",
    "age": 21,
    "major": "Computer Science"
}


# Adding a new key-value pair
student["GPA"] = 3.8

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

print(student.keys())
print(student.values())

