n=int(input("Hit me with your number man:"))
og_num=n
count=0
arms=0
while n>0:
    count+=1
    n=n//10
print(count)
n=og_num
while n>0:
    rem=n%10
    arms+=(rem)(count)
    n=n-rem
    n=n//10
    count-=1
