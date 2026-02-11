import csv

filename = "StudentDetails.csv"

def load_students(filename):
    students = []   
    with open(filename,"r") as file :
        reader = csv.DictReader(file)
        for row in reader :
            row["roll_no"] = int(row["roll_no"])
            row["name"] = row["name"]
            row["marks"] = int(row["marks"])
            students.append(row)
    print("Data Loaded Successfully.")

    return students

def add_students(students):
    roll_no = int(input("Enter roll number : "))
    name = input("Enter name : ")
    marks = int(input("Enter marks : "))

    students.append({
        "roll_no" : roll_no,
        "name" : name,
        "marks" : marks
    })

    print("Student is added succesfully.")

def display_students(students):
    if not students:
        print("No Student records found.")
        return
    print("\nRoll Number\tName\tMarks")
    print("-" * 25)

    for s in students:
        print(f"{s['roll_no']}\t{s['name']}\t{s['marks']}")

def delete_students(students):
    roll_no = int(input("Enter the roll number to delete : "))
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student Deleted Successfully.")
            return
        
    print("Student Not Found.")

def analytics(students) :
    if not students :
        print("No Data Available.")
        return 
    
    total = len(students)
    avg_marks = sum(s["marks"] for s in students) / total
    highest = max(s["marks"] for s in students)

    print("Total students :", total)
    print("Average marks :", avg_marks)
    print("Highest Marks : ", highest)

def save_students(filename, students) :
    with open(filename, 'w', newline = "") as file :
        fieldnames = ["roll_no", "name", "marks"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)

        writer.writeheader()
        writer.writerows(students)
    print("Data saved to file")

def menu():
    print("\n----Student Record Management System----")
    print("1.Load the data from file")
    print("2. Add new students.")
    print("3. Display Students and Details.")
    print("4. Delete Student by their roll number.")
    print("5. Analytics")
    print("6. Save & Exit")

students = load_students(filename)

while True:
    menu()
    choice = input("Enter your choice : ")

    if choice == "1":
        students = load_students(filename)
    elif choice == "2":
        add_students(students)
    elif choice == "3":
        display_students(students)
    elif choice == "4":
        delete_students(students)
    elif choice == "5":
        analytics(students)
    elif choice == "6":
        save_students(filename, students)
        break
    else:
        print("Invalid Choice") 



