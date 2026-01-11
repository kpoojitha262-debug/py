def add_student(students):
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = list(map(int, input("Enter 3 marks separated by space: ").split()))
    students[roll] = {"name": name, "marks": marks}

def display_students(students):
    for roll, data in students.items():
        avg = sum(data["marks"]) / len(data["marks"])
        print(f"Roll: {roll}, Name: {data['name']}, Average: {avg:.2f}")

students = {}

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student(students)
    elif choice == 2:
        display_students(students)
    elif choice == 3:
        break
    else:
        print("Invalid choice")
