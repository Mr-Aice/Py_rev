import csv
with open("file_handling/csv/sample.csv", "a+") as f:
    name: str = input("Enter Name: ")
    email: str = input("Enter Email: ")
    marks: int = int(input("Enter marks: "))
    medals: int = int(input("Enter medials: "))

    injector = csv.writer(f)
    injector.writerow([name, email, marks, medals])
print("Data inserted successfully!!!!")
