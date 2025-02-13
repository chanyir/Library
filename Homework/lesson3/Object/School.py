import Student
class Scool:
    def __init__(self, students=[]):
        self.students=students

    def add_student(self, new_student):
        flag=False
        for s in self.students:
            if new_student.id==s.id:
                return
        self.students.append(new_student)
    
    def print_students(self):
        for s in self.students:
            s.print_student()