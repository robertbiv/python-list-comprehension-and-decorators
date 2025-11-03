# Robert Bennethum
# MODEL
class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

# VIEW
def show_menu():
    print("\n1. View courses")
    print("2. Register")
    print("3. Drop")
    print("4. View schedule")
    print("5. Exit")

def display_courses(course_list):
    print("\nCourses:")
    for course in course_list:
        print(f"- {course.code}: {course.name}")

def display_schedule(student):
    print(f"\n{student.name}'s Schedule:")
    if student.courses:
        for course in student.courses:
            print(f"- {course.code}: {course.name}")
    else:
        print("No courses.")

# CONTROLLER
class RegistrationController:
    def __init__(self, student, courses):
        self.student = student
        self.courses = courses

    def register(self, course_code):
        for course in self.courses:
            if course.code == course_code and course not in self.student.courses:
                self.student.courses.append(course)
                print(f"Registered: {course.code}")
                return
        print("Not found or already registered")

    def drop(self, course_code):
        for course in self.student.courses:
            if course.code == course_code:
                self.student.courses.remove(course)
                print(f"Dropped: {course.code}")
                return
        print("Not in schedule")

# Main
courses = [
    Course("CMPSC101", "Intro to Computer Science"),
    Course("CMPSC102", "Data Structures"),
    Course("CMPSC103", "Algorithms")
]

name = input("Name: ")
student = Student(name)
controller = RegistrationController(student, courses)

# Loop
while True:
    show_menu()
    choice = input("Choice: ")
    
    if choice == "1":
        display_courses(courses)
    elif choice == "2":
        code = input("Course code: ")
        controller.register(code)
    elif choice == "3":
        code = input("Course code: ")
        controller.drop(code)
    elif choice == "4":
        display_schedule(student)
    elif choice == "5":
        break
    else:
        print("Invalid")
