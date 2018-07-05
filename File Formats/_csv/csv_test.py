import csv

with open("data.csv", newline='') as csv_file:
    reader = csv.reader(csv_file)
    for raw in reader:
        print(", ".join(raw))