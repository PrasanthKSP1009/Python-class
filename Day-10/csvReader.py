import csv

with open("Day-10/StudentsData.csv",'r') as data:
    reader = csv.reader(data)
    for row in reader:
        print(row)

    