
class Person:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self._age = age           # protected attribute

    def get_details(self):
        return f"Name: {self.name}, Age: {self._age}"


class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def get_details(self):
        return f"Student {self.name} | Age: {self._age} | ID: {self.student_id} | Grade: {self.grade}"



class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.__salary = salary     # private attribute

    def get_details(self):
        return f"Teacher {self.name} | Age: {self._age} | Subject: {self.subject}"

    
    def get_salary(self):
        return f"{self.name}'s Salary: Rs. {self.__salary}"


def main():
    # Creating objects
    student1 = Student("Asmita", 21, "STU101", "A")
    teacher1 = Teacher("Mr.Sharma", 40, "Python", 60000)

    print("---- Student Details ----")
    print(student1.get_details())

    print("\n---- Teacher Details ----")
    print(teacher1.get_details())
    print(teacher1.get_salary())   # accessing private data safely


if __name__ == "__main__":
    main()
