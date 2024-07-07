import csv

def gpa(marks):
    if 80 <= marks <= 100:
        return "A+"
    elif 70 <= marks <= 79:
        return "A"
    elif 60 <= marks <= 69:
        return "A-"
    elif 50 <= marks <= 59:
        return "B"
    elif 40 <= marks <= 49:
        return "C"
    elif 33 <= marks <= 39:
        return "D"
    elif 0 <= marks <= 32:
        return "F"

# Read the students names and marks from the input csv file->
students = []

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    students.append(header)
    for row in reader:
        students.append([row[0], int(row[1])])

    for row in students:
        print(row)

# Calculate grade for each student->
students_with_grade = []

for name, marks in students[1:]:
    grade = gpa(marks)
    students_with_grade.append([name, marks, grade])

# Write the students names, marks, and their grade to a new output csv file->
with open('result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Mark', 'Grade'])
    writer.writerows(students_with_grade)



