import csv


def grade_from_mark(mark):
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


def process_grades(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)    #  reader = csv.DictReader(infile)
        next(reader)
        writer = csv.writer(outfile)
        writer.writerow(['Name', 'Mark', 'Grade'])

        for row in reader:
            
            print(row[0])
            
            name = row[0]
            mark = int(row[1])
            grade = grade_from_mark(mark)
            writer.writerow([name, mark, grade])
           


input_file = 'students.csv'
output_file = 'result.csv'
process_grades(input_file, output_file)
