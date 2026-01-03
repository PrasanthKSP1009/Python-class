import csv

with open("Day-10/StudentsData.csv",'w') as data:
    writer = csv.writer(data)
    writer.writerow(["S.No","Name","Dept"])
    writer.writerow([1,"Prasanth","CSE"])
    writer.writerow([2,"Mahimithran","MSc DS"])
    writer.writerow([3,"Kanishma","MSc DS"])