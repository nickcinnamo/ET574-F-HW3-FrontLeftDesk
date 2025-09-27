

def read_students(file_path):
    names = []
    gpas = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    name = parts[0]
                    try:
                        gpa = float(parts[1])
                        names.append(name)
                        gpas.append(gpa)
                    except ValueError:
                        print(f"Invalid GPA for {name}. Skipping.")
                else:
                    print(f"Invalid line format: {line.strip()}")
    except FileNotFoundError:
        print("File not found.")
    return names, gpas

def calculate_average(gpas):
    if not gpas:
        return 0.0
    return sum(gpas) / len(gpas)

def print_above_average(names, gpas, average):
    print("\nStudents with above average GPA:")
    for name, gpa in zip(names, gpas):
        if gpa > average:
            print(f"{name}: {gpa}")

def predict_scholarship(names, gpas):
    print("\nStudents predicted to earn a scholarship (GPA ≥ 3.7):")
    for name, gpa in zip(names, gpas):
        if gpa >= 3.7:
            print(f"{name}: {gpa}")

def main():
    file_path = "students.txt"
    names, gpas = read_students(file_path)

    if not names:
        print("No student data available.")
        return

    average_gpa = calculate_average(gpas)
    print(f"\nAverage GPA: {average_gpa:.2f}")

    print_above_average(names, gpas, average_gpa)
    predict_scholarship(names, gpas)

if __name__ == "__main__":
    main()

# Step 1: Open and read the file
file = open("students.txt", "r")
lines = file.readlines()
file.close()

# Step 2: Create empty lists for names and GPAs
names = []
gpas = []

# Step 3: Process each line and fill the lists
for line in lines:
    parts = line.strip().split()
    names.append(parts[0])
    gpas.append(float(parts[1]))

# Step 4: Calculate average GPA
total_gpa = sum(gpas)
average_gpa = total_gpa / len(gpas)
print("Average GPA:", round(average_gpa, 2))

# Step 5: Print students with above-average GPA
print("\nAbove Average Students:")
for i in range(len(gpas)):
    if gpas[i] > average_gpa:
        print(names[i], "-", gpas[i])

# Step 6: Predict scholarship students (GPA >= 3.7)
print("\nScholarship Candidates:")
for i in range(len(gpas)):
    if gpas[i] >= 3.7:
        print(names[i], "-", gpas[i])

# Lists to store student names and GPAs
students = ["Jon", "Kim", "Lee", "Sara", "Miko", "Lin", "Toby", "Ben", "Mark", "Xia"]
gpas = [3.25, 2.25, 2.30, 4.00, 1.90, 2.10, 2.89, 2.75, 2.34, 3.53]

# Calculate average GPA
total = gpas[0] + gpas[1] + gpas[2] + gpas[3] + gpas[4] + gpas[5] + gpas[6] + gpas[7] + gpas[8] + gpas[9]
average = total / 10

print("Average GPA:", average)

print("\nStudents with above average GPA:")
# Check and print students with GPA above average
if gpas[0] > average:
    print(students[0], "-", gpas[0])
if gpas[1] > average:
    print(students[1], "-", gpas[1])
if gpas[2] > average:
    print(students[2], "-", gpas[2])
if gpas[3] > average:
    print(students[3], "-", gpas[3])
if gpas[4] > average:
    print(students[4], "-", gpas[4])
if gpas[5] > average:
    print(students[5], "-", gpas[5])
if gpas[6] > average:
    print(students[6], "-", gpas[6])
if gpas[7] > average:
    print(students[7], "-", gpas[7])
if gpas[8] > average:
    print(students[8], "-", gpas[8])
if gpas[9] > average:
    print(students[9], "-", gpas[9])

print("\nStudents predicted to earn a scholarship (GPA >= 3.5):")
# Scholarship prediction: GPA >= 3.5
if gpas[0] >= 3.5:
    print(students[0])
if gpas[1] >= 3.5:
    print(students[1])
if gpas[2] >= 3.5:
    print(students[2])
if gpas[3] >= 3.5:
    print(students[3])
if gpas[4] >= 3.5:
    print(students[4])
if gpas[5] >= 3.5:
    print(students[5])
if gpas[6] >= 3.5:
    print(students[6])
if gpas[7] >= 3.5:
    print(students[7])
if gpas[8] >= 3.5:
    print(students[8])
if gpas[9] >= 3.5:
    print(students[9])


