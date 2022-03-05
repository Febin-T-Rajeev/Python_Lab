header=[]
data=[]
import csv
with open("sample.csv","r") as f1:
    csvrdr=csv.reader(f1)
    header=next(csvrdr)
    print(header)
    for row in csvrdr:
        print(row)
        print(" ".join(row))
