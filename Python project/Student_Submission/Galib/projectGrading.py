#Step-1 Make a function that can calculate the grades

import csv

def grade(marks):
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


#Step-2 Read the CSV file and kinda append something

s = []

"""

IF YOU WANT YOU CAN CALCULATE GRADES OF ANY RESULT BY USING THIS WHATEVER. BUT YOU HAVE MAKE A CSV FILE , THE NAME MUST BE IN THE FIRST COLUMN AND THE MARKS MUST BE IN sECON COLUMN!!!!!!!!!!!!!!!!!

"""
with open('assets/students.csv', 'r') as file: 
    reader = csv.reader(file)
    header = next(reader)
    s.append(header)
    for row in reader:
        s.append([row[0], int(row[1])])

#Step-3 Time to cook the grades

s_grade= []

for name, marks in s[1:]:
    grades = grade(marks)
    s_grade.append([name, marks, grades])

#Break a Leg 

with open('assets/resultWithGrades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Mark', 'Grade'])
    writer.writerows(s_grade)



    



