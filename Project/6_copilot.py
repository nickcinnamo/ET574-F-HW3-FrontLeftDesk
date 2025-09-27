# Store names and GPAs in separate lists
names = ["Jon", "Kim", "Lee", "Sara", "Miko", "Lin", "Toby", "Ben", "Mark", "Xia"]
gpas = [3.25, 2.25, 2.30, 4.00, 1.90, 2.10, 2.89, 2.75, 2.34, 3.53]

# Calculate the average GPA
total = 0
for gpa in gpas:
    total += gpa
average = total / len(gpas)
print("Average GPA:", round(average, 2))

# Print above-average students
print("\nAbove average students:")
for i in range(len(gpas)):
    if gpas[i] > average:
        print(names[i], "-", gpas[i])

# Predict scholarship students (GPA >= 2.75)
print("\nScholarship recipients (predicted):")
for i in range(len(gpas)):
    if gpas[i] >= 2.75:
        print(names[i], "-", gpas[i])
