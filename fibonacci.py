#fibonacci
i=int(input())
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(2,i+1):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    
