for i in range(2,50):
    for j in range(1,50):
        a=pow(i,2)-pow(j,2)
        b=2*i*j
        c=pow(i,2)+pow(j,2)
        if a>0 and a<100 and b>0 and b<100 and c>0 and c<100:
            print(a,b,c)