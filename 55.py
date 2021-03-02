import random as rm

def printMatrix(ma):
    n=len(ma)
    for i in range(n):
        print(ma[i])

def getMatrix():
    n=5
    m=5
    ma=[[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            ma[i][j]=rm.randrange(1,10,4)
    return ma
if __name__ == '__main__':

    printMatrix(getMatrix())