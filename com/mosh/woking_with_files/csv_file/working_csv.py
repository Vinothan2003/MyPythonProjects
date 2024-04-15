import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)  # read the file
    print(list(reader))
    for data in reader:
        print(data)
    """writer = csv.writer(file) # override the file
    writer.writerow(["ID", "name", "age"])
    writer.writerow([2002141, "Vinothan NC", 20])
    writer.writerow([2002111, "asfasfas", 23])"""
