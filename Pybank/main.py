import csv

with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print(row)