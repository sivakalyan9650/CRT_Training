n=1634
def func1(n):
    if n==0:
        return 0
    return 1+func1(n//10)
count=func1(n)
def func2(n,count):
    if n==0:
        return 0
    return (n%10)**count+func2(n//10,count)
        
print(func2(n,count))
