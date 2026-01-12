import csv
with open("file_handling/csv/sample.csv", "r") as f:

    retriver = csv.reader(f)
    for line in retriver:
        print(line[0], line [1], line[2], line[3], sep='\t')
print("Data retrived successfully!!!!")