"""
write a recursive program to print the digits of a number in reverse order
def func(n):
    ldig=n%10
    print(ldig,end="")
    n=n//10
    while n>0:
        return func(n)
n=int(input("enter a number:"))
func(n)
"""
n=1452
def func(n):
    if n==0:
        return
    print(n%10)
    return func(n//10)
func(n)
