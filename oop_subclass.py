class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("init:{}".format(self.name))

    def tell(self):
        print("Name:{} Age:{}".format(self.name,self.age),end=" ")


class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print("init Teacher:{}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("salary:{}".format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print("init Student:{}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Mark:{}".format(self.marks))

t = Teacher('DLS',40,30000)

s = Student('ST',25,75)

print()

members = [t,s]

for member in members:
    member.tell()
