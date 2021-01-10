def isPrime(num):
    flag=1
    for i in range(2,num):
        if(num%i==0):
            flag=0
            break
    if flag==1 :
        print("{} is a Prime Number".format(num))
    elif flag==0 :
        print("{} is Not a Prime Number".format(num))

arr=[]
for i in range(2,51):
    flag=1
    for j in range(2,i):
        if(i%j==0):
            flag=0
            break  
    if flag==1:
        arr.append(i)
print(arr)
x=input("ENTER A NUMBER TO CHECK :")
isPrime(int(x))
