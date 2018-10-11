class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print('Initializing ', self.name)
        Robot.population += 1

    def die(self):
        print('%s is being killed' % self.name)
        Robot.population -= 1

        if Robot.population == 0:
            print('%s was the last robot' % self.name)
        else:
            print('There are still %d robots left' % Robot.population)

    def say_hi(self):
        print("Greetings, my masters call me % s" % self.name)

    @classmethod
    def how_many(cls):
        print('We have %d robots left!' % Robot.population)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()


