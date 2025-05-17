# Creating a student class with encapsulation, inheritance, and polymorphism
class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.__gpa = gpa  # Encapsulated (private) attribute

    # Method to access GPA (encapsulation)
    def get_gpa(self):
        return self.__gpa

    def update_gpa(self, new_gpa):
        if 0.0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
            print(f"{self.name}'s GPA updated to {self.__gpa}")
        else:
            print("Invalid GPA value.")

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}, GPA: {self.__gpa}")

# Subclass (inheritance + polymorphism)
class GraduateStudent(Student):
    def __init__(self, name, student_id, gpa, thesis_title):
        super().__init__(name, student_id, gpa)
        self.thesis_title = thesis_title

    # Polymorphism: override display_info
    def display_info(self):
        super().display_info()
        print(f"Thesis Title: {self.thesis_title}")

# Create student objects
student1 = Student("Alice", "S101", 3.6)
student2 = Student("Bob", "S102", 3.2)
grad_student = GraduateStudent("Charlie", "G201", 3.8, "Machine Learning in Education")

# Use methods
student1.display_info()
student1.update_gpa(3.9)

print("\n---------------------\n")

student2.display_info()
student2.update_gpa(2.5)

print("\n---------------------\n")

grad_student.display_info()
grad_student.update_gpa(3.95)



# Activity 2: polymorphism challenge
class Mover:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Animal classes
class Dog(Mover):
    def move(self):
        print("Running")

class Fish(Mover):
    def move(self):
        print("Swimming")

# Vehicle classes
class Car(Mover):
    def move(self):
        print("Driving")

class Plane(Mover):
    def move(self):
        print("Flying")

# Using polymorphism
def show_movement(movers):
    for mover in movers:
        mover.move()

# List of different movers
movers = [Dog(), Fish(), Car(), Plane()]

# Demonstrate polymorphic behavior
show_movement(movers)















































































