a=int(input())
temp=a
temp1=a
count=0
while a>0:
    count=count+1
    a=a//10
sum=0
while temp1>0:
    digit=temp1%10
    sum=sum+(digit**count)
    temp1=temp1//10
if temp==sum:
    print("armstrong")
else:
    print("not an armstrong")
    
