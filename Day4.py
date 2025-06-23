import csv

data = [
        ["Name","Age","Country"],
        ["Shivam","19","India"],
        ["Lakshay","20","Iran"],
        ["Sanidhya","19","canada"]
]

with open("writer.csv",'w') as file:
    writer = csv.writer(file)
    for row in data :
        writer.writerow(row)
try :
    n1 = int(input("enter the number "))
    y = 25 / n1
    print(y)
except ZeroDivisionError:
    print("Division by zero")





