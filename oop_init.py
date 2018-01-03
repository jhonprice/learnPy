class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('Hello,name is',self.name)

p = Person("Kazi")
p.say_hi()
