class Robot:
    population = 0

    def __init__(self,name):
        self.name = name
        print("Init {0}".format(self.name))

        population = 10
        
        Robot.population +=1

        print("po {0} ropo {1}".format(population,Robot.population))

    def die(self):

        print("{0} is KIA".format(self.name))

        Robot.population  -= 1

        if Robot.population == 0:
            print("{0} was the last one.".format(self.name))
        else:
            print("{id:d} working".format(id=Robot.population))

    def say_hi(self):
        print("greetings {0}".format(self.name))

    @classmethod
    def how_many(cls):
        print("sum is {:d}".format(cls.population))
