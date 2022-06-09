import math
import numpy as np
pi=math.pi
# function in question
def sam(x):
    if 0<=x<=0.1:
        return x**3+1
    elif 0.1<x<=0.2:
        return 1.001+0.03*(x-0.1)+0.3*(x-0.1)**2+2*(x-0.1)**3
    else :
        return 1.009+0.15*(x-0.2)+0.9*(x-0.2)**2+2*(x-0.2)**3
# romberg integration
def Romberg(a,b,n):
    # generate a 2xn matrix 
    M = [[0.5]*(n+1) for _ in range(3)]
    M=np.mat(M)
    # initialization
    h=b-a
    M[1,1]=h/2*(sam(a)+sam(b))
    print("%.6f" %M[1,1])
    for i in range(2,n+1):
        temp=0
        for k in range(1,2**(i-2)+1):
            temp=temp+sam(a+(k-0.5)*h)
        M[2,1]=1/2*(M[1,1]+h*temp)
        print("%.6f" %M[2,1],end="    ")
        for j in range(2,i):
            M[2,j]=M[2,j-1]+(M[2,j-1]-M[1,j-1])/(4**(j-1)-1)
            print(M[2,j],end="    ")
        M[2,i]=M[2,i-1]+(M[2,i-1]-M[1,i-1])/(4**(i-1)-1)
        print("%.6f" %M[2,i])
        h=h/2
        for j in range(1,i+1):
            M[1,j]=M[2,j]
        if abs(M[1,i-1]-M[2,i])<0.0001:
            print("The prodecure stops at n=",i,".")
            return
Romberg(0,0.3,100)





