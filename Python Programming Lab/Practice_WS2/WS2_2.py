list=[12,24,35,24,88,120,155]
num=[]
for i in list:
    if int(i) != 24:
        num.append(i)
print(num)