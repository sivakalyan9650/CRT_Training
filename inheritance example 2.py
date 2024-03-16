# create a class of name placements which has function info which displays the number of placements
#create another class name dept with function display which will display names of the departments present in college.
#create a class pragati with the function welcome which display welcome to pragati and
#this pragati class should also display the details about departments and placements

class placements:
    def info(self):
        print("623 and still couting")
class dept:
    def display(self):
        print("it dept,cse-dept,civil dept,ece dept")
class pragati(placements,dept):
    
    def welcome(self):
        print("welcome to pragati")
    


obj2=pragati()
obj2.welcome()
obj2.display()
