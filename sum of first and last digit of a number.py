#write a function to calculate sum of first and last digit of a number

def sum1(a):
    last=a%10
    while a>10:
        a=a//10
    print(last+a)
sum1(int(input("enter a number:")))
        
    
    
