import math

def getinput(a):
    a=list(a)
    for i in range(n):
        a.append(int(input("ENTER THE {}' ELEMENT :".format(i+1))))
    return tuple(a)

def euclideanDistance(u,v):
    sum=0
    for i in range(n):
        sum+=pow(v[i]-u[i],2)
    return math.sqrt(sum)

if __name__=="__main__":
    u=()
    v=()
    n=int(input("ENTER THE VALUE OF N:"))
    print("ENTER THE ELEMENTS OF U:")
    u=getinput(u)
    print("ENTER THE ELEMENTS OF V:")
    v=getinput(v)
    print(str(euclideanDistance(u,v))+" IS THE EUCLIDEAN DISTANCE")
