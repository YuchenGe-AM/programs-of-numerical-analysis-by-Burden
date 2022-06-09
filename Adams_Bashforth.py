import math
import numpy as np
from sympy import *
from matplotlib import pyplot as plt
# Adams_Bashforth's method
def f(t,y):
    return -(y+1)*(y+3)
def y(t):
    return -3+2*(1+math.exp(-2*t))**(-1)
def Adams_Bashforth(a,b,N,alpha):
    w = [[0.5]*(N+10) for a in range(6)]
    w=np.mat(w)
    h=(b-a)/N
    t=a
    w[2,0]=alpha
    w[2,1]=-1.90033209
    w[3,0]=alpha
    w[3,1]=-1.90033209
    w[3,2]=-1.80262486
    w[4,0]=alpha
    w[4,1]=-1.90033209
    w[4,2]=-1.80262486
    w[4,3]=-1.70868768 
    w[5,0]=alpha
    w[5,1]=-1.90033209
    w[5,2]=-1.80262486
    w[5,3]=-1.70868768 
    w[5,4]=-1.62005146
    k=0
    for i in range(1,N):
        w[2,i+1]=w[2,i]+h/2*(3*f(t,w[2,i])-f(t-h,w[2,i-1]) )
        w[3,i+2]=w[3,i+1]+h/12*(23*f(t,w[3,i+1])-16*f(t-h,w[3,i])+5*f(t-2*h,w[3,i-1]) )
        w[4,i+3]=w[4,i+2]+h/24*(55*f(t,w[4,i+2])-59*f(t-h,w[4,i+1])+37*f(t-2*h,w[4,i])-9*f(t-3*h,w[4,i-1]) )
        w[5,i+4]=w[5,i+3]+h/720*(1901*f(t,w[5,i+3])-2774*f(t-h,w[5,i+2])+2616*f(t-2*h,w[5,i+1])-1274*f(t-3*h,w[5,i])+251*f(t-4*h,w[5,i-1]))
        t=a+i*h
        k=k+0.1
        print("%.1f & %.8f &%.8f &%.8f & %.8f & %.8f\\\\" %(k,y(k),w[2,i],w[3,i],w[4,i],w[5,i]) )
Adams_Bashforth(0,2,20,-2)
