#write a program to check the type of triangle
#where you take the input from user for 3 sides
#classify into equlateral,lsoceles and scalen

a=int(input("enter 1st side:"))
b=int(input("enter 2st side:"))
c=int(input("enter 3st side:"))
if a==b==c:
    print("equlateral")
elif (a==b and a!=c)or(b==c and b!=a)or(c==a and a!=b):
    print("isoceles")
elif a!=b!=c :
    print("scalen")


      
