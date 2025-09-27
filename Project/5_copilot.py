# List of student names
students = ["Jon", "Kim", "Lee", "Sara", "Miko", "Lin", "Toby", "Ben", "Mark", "Xia"]

# List of corresponding GPAs
gpas = [3.25, 2.25, 2.30, 4.00, 1.90, 2.10, 2.89, 2.75, 2.34, 3.53]

# Calculate average GPA
total_gpa = sum(gpas)
count = len(gpas)
average_gpa = total_gpa / count

print("Average GPA:", average_gpa)

# Print students with above average GPA
print("\nStudents with above average GPA:")
for i in range(count):
    if gpas[i] > average_gpa:
        print(students[i], "-", gpas[i])

# Predict scholarship eligibility (GPA >= 3.5)
print("\nStudents eligible for scholarship:")
for i in range(count):
    if gpas[i] >= 3.5:
        print(students[i], "-", gpas[i])
