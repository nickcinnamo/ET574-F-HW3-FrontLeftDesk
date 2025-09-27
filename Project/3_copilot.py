
def read_students(filename):
    """Read student names and GPAs from a file."""
    students = []
    gpas = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                if ',' in line:
                    name, gpa_str = line.strip().split(',')
                    try:
                        gpa = float(gpa_str)
                        students.append(name.strip())
                        gpas.append(gpa)
                    except ValueError:
                        print(f"Invalid GPA for {name}: {gpa_str}")
                else:
                    print(f"Ignoring invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return [], []

    return students, gpas


def compute_average(gpas):
    """Compute average GPA from the list."""
    if not gpas:
        return 0
    return sum(gpas) / len(gpas)


def print_above_average(students, gpas, avg_gpa):
    """Print students with GPA above the average."""
    print("\nStudents with above average GPA:")
    for name, gpa in zip(students, gpas):
        if gpa > avg_gpa:
            print(f"{name}: {gpa}")


def predict_scholarship(students, gpas, threshold=3.7):
    """Predict which students may earn a scholarship based on GPA threshold."""
    print("\nPredicted scholarship recipients (GPA >= {:.1f}):".format(threshold))
    for name, gpa in zip(students, gpas):
        if gpa >= threshold:
            print(f"{name}: {gpa}")


# --- Main Program ---
filename = "students.txt"
students, gpas = read_students(filename)

if students:
    avg_gpa = compute_average(gpas)
    print(f"\nAverage GPA: {avg_gpa:.2f}")

    print_above_average(students, gpas, avg_gpa)
    predict_scholarship(students, gpas)
else:
    print("No valid student data found.")
