import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.helth_level = random.random()

    def say_hi(self):
        print('Hi, I am, ' + self.name)

    def needs_a_doctor(self):
        if self.helth_level < 0.8:
            return True
        else:
            return False
    
class PysicianRobot(Robot):
    
    def say_hi(self):
        super().say_hi()
        print('and I am a physician!')
        # print('Everything will be okay')
        # print(self.name + 'takes care of you.')

    # robo here is parent class data
    def heal(self, robo):
        robo.helth_level = random.uniform(robo.helth_level, 1)
        print(robo.name + ' has been healed by ' + self.name + '!')

# create child class's object

doc = PysicianRobot('Dr. Suraj Patel')
doc.say_hi()
# creat empty list to get all results at once
rob_list = []

for i in range(5):
    x = Robot("Pacent" + str(i))
    if x.needs_a_doctor():
        print('health_level of ' + x.name + ' befor healing ', x.helth_level)
        doc.heal(x)
        print('helth_level of ' + x.name + ' after healing ', x.helth_level)
    rob_list.append((x.name, x.helth_level))

print('Rob List: ',rob_list)
