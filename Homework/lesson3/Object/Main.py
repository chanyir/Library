import Student
import School

s1=Student.Student("chany",111,[100,98,95])
s2=Student.Student("pniny",222,[100,99,96])
s3=Student.Student("esty",333,[100,99,100])

scool=School.Scool([s1,s2])

scool.print_students()
scool.add_student(s3)
scool.print_students()

# s.print_student()
# s.add_grade(92)
# s.print_student()
# print(s.get_avg())

