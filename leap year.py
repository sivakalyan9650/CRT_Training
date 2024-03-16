#check if a given year is leap or not
#if the year is divisible by 4 and not divisible by 100 or if it is divisible by 400 then it is called a leap year
a=int(input())
if a%4==0 and a%100!=0:
    print("leap")
elif a%400==0 :
    print("leap")
else:
    print("not a leap")
