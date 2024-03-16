# function overloading in python
class arithmetic:
    def sum(self,a):
        print(a)
    def sum(self,a,b):
        print(b-a)
    def sum(self,a,b,c):
        print(a+b+c)
obj=arithmetic()
#obj.sum(10)
#obj.sum(10,20)
obj.sum(10,30,20)

