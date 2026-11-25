
students = []

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print("Student added successfully!")

def view_students():
    print("\nStudent List:")
    for student in students:
        print(student)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
    elif choice == "4":
    delete_student()
    else:
        print("Invalid choice")


def delete_student():
    name = input("Enter student name to delete: ")

    if name in students:
        students.remove(name)
        print("Student deleted successfully!")
    else:
        print("Student not found!")
print("4. Delete Student")


