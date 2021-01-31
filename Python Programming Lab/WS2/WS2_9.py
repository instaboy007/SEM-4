def abs(x):
    if isinstance(x,int):
        if x<0:
            return x*-1
        elif x>=0:
            return x
    if isinstance(x,float):
        if x<0:
            return x*-1
        elif x>=0:
            return x
    if isinstance(x,complex):
        return pow(x.imag*2+x.real*2,0.5)

if __name__=="__main__":
    print(abs(1+1j))
    print(abs(-1))
    print(abs(1))
