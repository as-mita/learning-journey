# Day 4 - Intermediate Python
# Student Management System using OOP + File Handling

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        return f"Name: {self.name}, Grade: {self.grade}"


class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    # Save student to file
    def add_student(self, student):
        with open(self.filename, "a") as file:
            file.write(f"{student.name},{student.grade}\n")
        print("\nStudent added successfully!")

    # Display all students
    def show_students(self):
        try:
            with open(self.filename, "r") as file:
                data = file.readlines()

            if not data:
                print("\nNo student records found!")
                return

            print("\n--- Student Records ---")
            for line in data:
                name, grade = line.strip().split(",")
                print(f"Name: {name}, Grade: {grade}")

        except FileNotFoundError:
            print("\nNo student records found!")

    # Search for a student
    def search_student(self, name):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    student_name, grade = line.strip().split(",")
                    if student_name.lower() == name.lower():
                        print("\nStudent found!")
                        print(f"Name: {student_name}, Grade: {grade}")
                        return
            print("\nStudent not found.")

        except FileNotFoundError:
            print("\nNo student records found!")


# -------- Main Program --------
def main():
    manager = StudentManager()

    while True:
        print("\n----- Student Manager -----")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            student = Student(name, grade)
            manager.add_student(student)

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_student(name)

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
