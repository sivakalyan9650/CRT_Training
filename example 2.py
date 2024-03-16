#take an int input from user
#if it is divisible by 3 and 6 print good number
#if it is divisible by 2 and 7 then print average
#divisible by 4 or 9 print awesome
#else bad 

a=int(input())
if a%3==0 and a%6==0:
    print("good number")
elif a%2==0 and a%7==0:
    print("average number")
elif a%4==0 or a%9==0:
    print("awesome number")
else:
    print("bad number")
    
