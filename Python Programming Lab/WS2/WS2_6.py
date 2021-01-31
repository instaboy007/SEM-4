import numpy as np

if __name__=="__main__":
    r=int(input("ENTER THE NUMBER OF ROWS :"))
    c=int(input("ENTER THE NUMBER OF COLUMNS :"))
    print("ENTER THE ELEMENTS OF THE MATRIX :")
    elements=list(map(int,input().split()))
    matrix = np.array(elements).reshape(r,c) 
    if np.linalg.det(matrix)==0:
        print("INVERSE DOESNT EXIT")
    else:
        print(np.linalg.inv(matrix)) 