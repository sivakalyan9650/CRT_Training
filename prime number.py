a=int(input())
count=0;
for i in range(2,a):
    if a%i!=0:
        count=count+1
if count==a-2:
        print("prime")
else:
        print("not a prime")
        

#optimized

"""
a=int(input())

flag=0
for i in range(2,a):
   if n%i==0:
    flag=1
    break
if flag==1:
  print("not prime")
else :
  print("prime")
"""
