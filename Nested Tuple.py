# Define a nested tuple
student = (
    ("Alice", 20, "Biology"),
    ("Bob", 22, "Mathematics"),
    ("Charlie", 19, "Physics")
)

# Accessing entire inner tuple
print("First student record:", student[0])

# Accessing individual elements inside the nested tuple
print("Second student's name:", student[1][0])
print("Third student's age:", student[2][1])
print("Third student's subject:", student[2][2])

# Looping through nested tuples
print("\nAll students:")
for s in student:
    name, age, subject = s
    print(f"{name} is {age} years old and studies {subject}.")