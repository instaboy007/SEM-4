i=2000
arr=[]
while i<=3200:
    if i%7==0 and i%5!=0:
        arr.append(str(i))
    i+=1
print(','.join(arr))    