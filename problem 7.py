#calculate the difference of sum of numbers that are divisible by 6 and not divisible by 6 in the range of 1-30
sum1=0
sum2=0
for i in range(1,31):
    if i%6==0:
        sum1=sum1+i
        
    else:
        sum2=sum2+i
        
print(sum2-sum1)
    
