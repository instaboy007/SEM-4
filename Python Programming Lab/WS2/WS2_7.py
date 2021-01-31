import numpy as np

def isSymmetric(matrix):
    if np.array_equal(matrix,np.transpose(matrix)):
        print("SYMMETRIC")
    else:
        print("NOT SYMMETRIC")

def isStochastic(matrix):
    if all(sum(row) == 1 for row in np.transpose(matrix)) and r==c:
        print("STOCHASTIC")
    else:
        print("NOT STOCHASTIC")

def isOrthogonal(matrix,r):
    transpose=np.transpose(matrix)
    matrixProd=np.matmul(transpose,matrix)
    identityMatrix=np.identity(r)
    if np.array_equal(identityMatrix,matrixProd):
        print("ORTHOGONAL")
    else:
        print("NOT ORTHOGONAL")

if __name__=="__main__":
    r=int(input("ENTER THE NUMBER OF ROWS :"))
    c=int(input("ENTER THE NUMBER OF COLUMNS :"))
    print("ENTER THE ELEMENTS OF THE MATRIX :")
    elements=list(map(float,input().split()))
    matrix = np.array(elements).reshape(r,c)
    isSymmetric(matrix)
    isStochastic(matrix)
    isOrthogonal(matrix,r)