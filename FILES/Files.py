import csv

filename = "stud.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["roll_no", "name", "marks"])
    writer.writerow([1,"Tahri",85])
    writer.writerow([2,"Alice",80])
    writer.writerow([3,"Priya",70])

with open(filename,"r") as csvfile:
    csvreader = csv.reader(csvfile)

    headers = next(csvreader)

    for row in csvreader:
        print(row)

with open(filename, "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

file.close() 
