#map function
def check(n):
    if n%2==0:
        return "yes"
    elif (n+1)%2==0:
        return "no"
    else:
        print("enter again")
a=map(check,[2,45,456,123,74])
print(list(a))


#note

split function
