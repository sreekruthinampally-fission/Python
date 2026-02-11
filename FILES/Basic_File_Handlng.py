import csv

fields = ['Name', 'Age', 'Location']
rows = [
    ['Nikhil', '25', 'Bombay'],
    ['Priya', '26', 'Goa' ]
]

with open("Deets.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

#data = [
    {'Name' : 'Nikhil', 'Location' : 'Bombay'}
    {'Name' : 'Priya', 'Location' : 'Goa'}
#]

fields = ['Name', 'Location']

with open("dictdeets.csv", "w") as fileyu:
    writer = csv.DictWriter(fileyu)

    writer.writeheader()
    writer.writerows() #data in brackets

