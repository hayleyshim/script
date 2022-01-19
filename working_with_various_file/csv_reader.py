import csv

with open('grade.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        this_grade = list()
        for grade in row[1:]:
            this_grade.append(int(grade))
        print('average of %s is %f' %(name, mean(this_grade)))