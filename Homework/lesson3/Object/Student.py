
class Student:
    def __init__(self,name,id,gradeas=[]):
        self.name=name
        self.id=id
        self.grades=gradeas
        self.max_grades=5

    def print_student(self):
        print(f'name:{self.name}, id:{self.id} her gradeas is:{self.grades} ')
        
        
    def add_grade(self, new_grade):
        if len(self.grades)<self.max_grades:
            self.grades.append(new_grade)

    def get_avg(self):
        total=0
        for i in self.grades:
            total+=i
        return total/len(self.grades)    
           



