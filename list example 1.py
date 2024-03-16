lis=[12,42,23,96,7,18,10,133]
min=133
max=7
for i in range(0,len(lis)):
    if lis[i]<min:
        min=lis[i]
    if lis[i]>max:
        max=lis[i]
print(min+max)
print(max-min)


