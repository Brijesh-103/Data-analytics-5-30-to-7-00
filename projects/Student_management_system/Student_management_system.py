import os
file_name = "students.txt"

if not os.path.exists(file_name):
    open(file_name, 'w').close()



def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    rollnumber = input("Enter student roll number: ")
    grade = input("Enter student grade: ")
    course = input("Enter student course: ")


    with open(file_name, 'a') as file:
        file.write(f"{name},{age},{rollnumber},{grade},{course}\n")

    print("===Student added successfully!===")

def view_students():
    with open(file_name, 'r') as file:
        students = file.readlines()

    if not students:
        print("No students found.")
        return

    for student in students:
        name, age, rollnumber, grade, course = student.strip().split(',')
        print(f"Name: {name}\n Age: {age} \n Roll Number: {rollnumber}\n Grade: {grade}\n Course: {course}\n\n")
    
def search_students():
    search_rollnumber = input("Enter student rollnumber to search: ")
    with open(file_name, 'r') as file:
        students = file.readlines()

    found_students = [student for student in students if search_rollnumber in student]

    if not found_students:
        print("No students found with that name.")
        return

    for student in found_students:
        name, age, rollnumber, grade, course = student.strip().split(',')
        print(f"Name: {name}, Age: {age}, Roll Number: {rollnumber}, Grade: {grade}, Course: {course}")

def update_students():
    search_rollnumber = input("Enter student rollnumber to update: ")
    with open(file_name, 'r') as file:
        students = file.readlines()

    updated_students = []
    found = False

    for student in students:
        name, age, rollnumber, grade, course = student.strip().split(',')
        if rollnumber == search_rollnumber:
            found = True
            print("Enter new details (leave blank to keep current value):")
            new_name = input(f"Name ({name}): ") or name
            new_age = input(f"Age ({age}): ") or age
            new_grade = input(f"Grade ({grade}): ") or grade
            new_course = input(f"Course ({course}): ") or course
            updated_students.append(f"{new_name},{new_age},{rollnumber},{new_grade},{new_course}\n")
        else:
            updated_students.append(student)

    if not found:
        print("No students found with that roll number.")
        return

    with open(file_name, 'w') as file:
        file.writelines(updated_students)

    print("Student updated successfully!")

def delete_students():
    search_rollnumber = input("Enter student rollnumber to delete: ")
    with open(file_name, 'r') as file:
        students = file.readlines()

    remaining_students = [student for student in students if search_rollnumber not in student]

    if len(remaining_students) == len(students):
        print("No students found with that roll number.")
        return

    with open(file_name, 'w') as file:
        file.writelines(remaining_students)

    print("Student deleted successfully!")


def main():
    while True:
        print("\n=============Student Management System=============")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Students")
        print("4. Update Students")
        print("5. Delete Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_students()
        elif choice == '4':
            update_students()
        elif choice == '5':
            delete_students()
        elif choice == '6':
            print("Thank you for using the Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


main()