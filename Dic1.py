# Dictionary of students with nested dictionaries
students = {
    "101": {
        "name": "Alice",
        "grades": [85, 90, 78],
        "major": "Math"
    },
    "102": {
        "name": "Bob",
        "grades": [88, 76, 92],
        "major": "Physics"
    },
    "103": {
        "name": "Charlie",
        "grades": [90, 95, 100],
        "major": "Computer Science"
    }
}

# Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Add average grade to each student
for student_id, data in students.items():
    avg = calculate_average(data["grades"])
    data["average"] = avg

# Find the top student
top_student = None
highest_avg = 0

for student_id, data in students.items():
    if data["average"] > highest_avg:
        highest_avg = data["average"]
        top_student = data["name"]

# Print all student data
print("Student Details:\n")
for student_id, data in students.items():
    print(f"ID: {student_id}")
    print(f"  Name: {data['name']}")
    print(f"  Major: {data['major']}")
    print(f"  Grades: {data['grades']}")
    print(f"  Average: {data['average']:.2f}")
    print()

print(f"🎓 Top Student: {top_student} with an average of {highest_avg:.2f}")
