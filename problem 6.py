#take a input number
#check if sum of factors of the number is greater than original number
#abundant
a=int(input())
sum=0
for i in range(1,(a//2)+1):
    if a%i==0:
        sum=sum+i
if a<sum:
    print("yes")
else:
    print("no")
    
