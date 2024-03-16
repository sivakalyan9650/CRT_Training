#write a program to check the onroad price of a bike
#if price > 72000 income tax is 10 % of original price+insurance will be 15%
#if price > 150000 income and < 200000 then tax is 25% + insurance 20%
#price > 200000 tax 35% +insurance 28%   otherwise enter a valid price
price=int(input())
if price>=72000 and price<150000:
    price+=(0.1*price)+(0.15*price)
    print("onroad price:",price)
elif price>=150000 and price<200000:
    price+=(0.25*price)+(0.2*price)
    print("onroad price:",price)
elif price>=200000:
    price+=(0.35*price)+(0.28*price)
    print("onroad price:",price)
else :
    print("enter a valid number")    
    

    
