class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def add_student(self, name, current_class):
        id = len(self.students) + 1
        student = Student(name, current_class, id)
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Student ID: {student.id}, Name: {student.name}, Class: {student.current_class}")

    def display_teachers(self):
        for teacher in self.teachers:
            print(f"Teacher ID: {teacher.id}, Name: {teacher.name}, Subject: {teacher.subject}")

phitron = School('samiul')

phitron.add_teacher('Sydz sir', 'DTC')
phitron.add_teacher('Anis sir', 'Database')
phitron.add_student('shakila mme', 'algorithm')

phitron.add_student('samiul', 1)
phitron.add_student('topu', 2)
phitron.add_student('rownok', 3)

print("Teachers:")
phitron.display_teachers()
print()
print("Students:")
phitron.display_students()
