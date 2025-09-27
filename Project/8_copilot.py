# Store students, majors, and GPAs in a dictionary
students = {
    "Jon": {"GPA": 3.25, "Major": "Math"},
    "Kim": {"GPA": 2.25, "Major": "Biology"},
    "Lee": {"GPA": 2.30, "Major": "Math"},
    "Sara": {"GPA": 4.00, "Major": "Math"},
    "Miko": {"GPA": 1.90, "Major": "Math"},
    "Lin": {"GPA": 2.10, "Major": "Biology"},
    "Toby": {"GPA": 2.89, "Major": "Biology"},
    "Ben": {"GPA": 2.75, "Major": "Math"},
    "Mark": {"GPA": 2.34, "Major": "Math"},
    "Xia": {"GPA": 3.53, "Major": "Biology"}
}

# Compute the average GPA
gpa_list = []
for name in students:
    gpa_list.append(students[name]["GPA"])
average_gpa = sum(gpa_list) / len(gpa_list)
print("Average GPA:", round(average_gpa, 2))

# Print all above average students
print("Above average students:")
for name in students:
    if students[name]["GPA"] > average_gpa:
        print(name, students[name]["GPA"], students[name]["Major"])

# Predict scholarship
print("Scholarship predictions:")
for name in students:
    gpa = students[name]["GPA"]
    major = students[name]["Major"]
    # Scholarship rules based on examples:
    # Biology majors with GPA >= 2.75 earn a scholarship
    # Math majors with GPA >= 3.5 earn a scholarship
    if major == "Biology" and gpa >= 2.75:
        print(name, "earned a scholarship.")
    elif major == "Math" and gpa >= 3.5:
        print(name, "earned a scholarship.")
    else:
        print(name, "did not earn a scholarship.")