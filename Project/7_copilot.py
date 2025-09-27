# Student names and GPAs
names = ['Jon', 'Kim', 'Lee', 'Sara', 'Miko', 'Lin', 'Toby', 'Ben', 'Mark', 'Xia']
gpas = [3.25, 2.25, 2.30, 4.00, 1.90, 2.10, 2.89, 2.75, 2.34, 3.53]

# Calculate average GPA
total = sum(gpas)
count = len(gpas)
average = total / count

print("Average GPA:", round(average, 2))
print()

# Print above average students
print("Above average students:")
for i in range(count):
    if gpas[i] > average:
        print(names[i], gpas[i])
print()

# Scholarship prediction based on examples
# From the examples:
# Jake 2.75 ✅
# Markus 2.90 ✅
# Teri 3.15 ✅
# Leigh 3.75 ✅
# So it seems: **Students with GPA >= 2.75 earn scholarships**

print("Scholarship predictions:")
for i in range(count):
    if gpas[i] >= 2.75:
        print(names[i], gpas[i], "- will earn a scholarship")
