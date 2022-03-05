import csv
with open("sample.csv","r") as f1:
    csvrdr=csv.reader(f1)
    for row in csvrdr:
        print(row[0],row[1],row[5])
