
a=int(input())
sum=0

temp=a
while a>0:
    digits=a%10
    sum=sum*10+digits
    a=a//10
    
if temp==sum:
    print("palindrome")
else:
    print("not")

