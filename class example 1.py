#create a class f15 with functions lights,fans and ac
#when lights is called print colour of the light which is taken as parameter to the function
#when fan is called it displays the fan regulator speed which taken as parameter of the function
#ac displays the room temeperature and outside temperature which are taken as parameters
#write display function which displays the difference in outside and room temperature of ac and also displays fan speed

class f15:
    def __init__(self,start,end):
        print("this is constructor")
        print("it executes automatically when object is created")
        self.st=start
        self.en=end
    def light(self,colour):
        print("the colour of light is:",colour)
    def fan(self,speed):
        self.c=speed
        #print("the speed of fan is:",speed)
    def ac(self,room,outside):
        self.a=room
        self.b=outside
        #print("room temerature:",room,"outside temperature:",outside)
    def display(self):
        print("the difference:",self.b-self.a)
        print("fan speed:",self.c)
        print("start time is:",self.st)
        print("end time is:",self.en)

obj1=f15(9,4)
#obj1.light("red")
obj1.fan(5)
obj1.ac(16,30)
obj1.display()
        
