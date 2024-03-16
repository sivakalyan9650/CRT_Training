#write a recursive function to count no of digits of a number
#write a recursive function to calculate sum of digits of a number

"""
a=12344563
def func1(a):
    if a<10:
        return 1
    return 1+func1(a//10)
print(func1(a))
"""

a=1458
def func2(a):
    if a==0:
        return 0
    return a%10+func2(a//10)
print(func2(a))

    
