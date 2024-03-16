#take int input from user
#check whether if the number is divisible by sum of digits or not
a=int(input())
temp=a
sum=0
while a>0:
    digit=a%10
    sum=sum+digit
    a=a//10
if temp%sum==0:
    print("true")
else:
    print("false")
