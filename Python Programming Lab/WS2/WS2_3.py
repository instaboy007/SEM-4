import math

def getinput(a):
    a=list(a)
    for i in range(n):
        a.append(float(input("ENTER THE {}' ELEMENT :".format(i+1))))
    return tuple(a)

def dot(u,v):
    dot=0
    for i in range(n):
        dot+=u[i]*v[i]
    return dot

def mod(a):
    mod=0
    for i in range(n):
        mod+=pow(a[i],2)
    return math.sqrt(mod)
    

def cosineAngle(u,v):
    return dot(u,v)/(mod(u)*mod(v))

def euclideanDistance(u,v):
    sum=0
    for i in range(n):
        sum+=pow(v[i]-u[i],2)
    return math.sqrt(sum)

if __name__=="__main__":
    u=()
    v=()
    n=int(input("ENTER THE DIMENSION OF THE VECTOR:"))
    print("ENTER THE ELEMENTS OF U:")
    u=getinput(u)
    print("ENTER THE ELEMENTS OF V:")
    v=getinput(v)
    print(str(cosineAngle(u,v))+" IS THE COSINE ANGLE")#measures the angel
    print(str(euclideanDistance(u,v))+" IS THE EUCLIDEAN DISTANCE")#measures the distance between points