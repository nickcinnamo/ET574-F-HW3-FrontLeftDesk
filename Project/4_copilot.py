Alice,3.9
Bob,3.4
Charlie,3.8
Diana,3.6
# Create empty lists to store names and GPAs
names = []
gpas = []

# Open and read data from the file
file = open("students.txt", "r")
lines = file.readlines()
file.close()

# Process each line in the file
for line in lines:
    line = line.strip()           # Remove newline characters
    parts = line.split(",")       # Split into name and GPA
    name = parts[0]
    gpa = float(parts[1])         # Convert GPA to float
    names.append(name)            # Add to names list
    gpas.append(gpa)              # Add to gpas list

# Calculate the average GPA
total = 0
for gpa in gpas:
    total += gpa
average = total / len(gpas)

# Print the average GPA
print("Average GPA:", round(average, 2))

# Print students with above average GPA
print("\nAbove average students:")
for i in range(len(gpas)):
    if gpas[i] > average:
        print(names[i], "-", gpas[i])

# Predict scholarship students (GPA ≥ 3.7)
print("\nScholarship candidates:")
for i in range(len(gpas)):
    if gpas[i] >= 3.7:
        print(names[i], "-", gpas[i])
