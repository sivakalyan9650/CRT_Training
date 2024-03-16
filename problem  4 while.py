a=int(input())
ans=1
while a>0:
    n=a%10
    ans=ans*n
    a=a//10
print(ans)

