import csv

def convert_mark_to_grade(mark):
    mark = int(mark)
    if 80 <= mark <= 100:
        return 'A+'
    elif 70 <= mark < 80:
        return 'A'
    elif 60 <= mark < 70:
        return 'A-'
    elif 50 <= mark < 60:
        return 'B'
    elif 40 <= mark < 50:
        return 'C'
    elif 33 <= mark < 40:
        return 'D'
    else:
        return 'F'


with open('students.csv', mode='r') as file:
    csvFile = csv.reader(file)
    lines = list(csvFile)
    ck=0
    for line in lines:
        if ck==0:
            ck=1
            continue
        line.pop()
        line.append(convert_mark_to_grade(line[1]))
        print(line)

with open('result.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for line in lines:
        writer.writerow(line)