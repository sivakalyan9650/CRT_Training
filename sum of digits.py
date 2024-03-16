#calculate the sum of digits of a number
a=int(input())
ans=0
while(a>0):
    temp=a
    ans+=(temp%10)
    a=a//10
print(ans)
