"""
   syntax:
def funname():
    statemnets

    function call
    funname()

    """
"""
#write a function which takes two arguments a and b type cast the value of second argument into integer then multiply them and print the last digit of the result

def func(a,b):
    b=int(b)
    print((a*b)%10)
func(12,13.256)
"""

#syntax of unknown arguments
def func(**name):
    print("my name is",name["fname"])
func(fname="siva",mname="kalyan",lname="reddy")
