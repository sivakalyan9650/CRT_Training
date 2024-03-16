#write a recursive function to count no of digits of a number
#write a recursive function to calculate sum of digits of a number

""" question 1 
n=725
def func(n):
    if n<10:
        return 1
    else:
        return 1+func(n//10)
print(func(n))
"""

n=1562

def func(n):
    if n<10:
        return n
    else:
        return n%10+func(n//10)
print(func(n))
