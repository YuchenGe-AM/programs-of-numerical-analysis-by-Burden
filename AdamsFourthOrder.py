import math
import numpy as np
from sympy import *
from matplotlib import pyplot as plt
# Adams Fourth-Order Predictor-Correct method
def f(t,y):
    return -(y+1)*(y+3)
def y(t):
    return -3+2*(1+math.exp(-2*t))**(-1)
def Adams_FourthOrder(a,b,N,alpha):
    w = [[0.5]*(N+10) for a in range(6)]
    w=np.mat(w)
    h=(b-a)/N
    t=[a+i*h for i in range(0,N+10)]
    t[0]=a
    w[1,0]=alpha
    w[2,0]=alpha
    w[3,0]=alpha
    w[4,0]=alpha
    k=0
    for i in range(1,4): # runge-Kutta
        K1=h*f(t[i-1],w[1,i-1])
        K2=h*f(t[i-1]+h/2,w[1,i-1]+K1/2)
        K3=h*f(t[i-1]+h/2,w[1,i-1]+K2/2)
        K4=h*f(t[i-1]+h,w[1,i-1]+K3)
        w[1,i]=w[1,i-1]+1/6*(K1+2*K2+2*K3+K4)
        w[2,i]=w[1,i]
        w[3,i]=w[1,i]
        w[4,i]=w[1,i]
    for i in range(3,N+1): # corrector
        w[1,i+1]=w[1,i]+h/24*(55*f(t[i],w[1,i])-59*f(t[i-1],w[1,i-1])+37*f(t[i-2],w[1,i-2])-9*f(t[i-3],w[1,i-3])   )
        w[1,i+1]=w[1,i]+h/24*(9*f(t[i+1],w[1,i+1])+19*f(t[i],w[1,i])-5*f(t[i-1],w[1,i-1])+f(t[i-2],w[1,i-2])   )
        w[2,i+1]=w[1,i]+h/24*(9*f(t[i+1],w[1,i+1])+19*f(t[i],w[1,i])-5*f(t[i-1],w[1,i-1])+f(t[i-2],w[1,i-2])   )
        w[3,i+1]=w[1,i]+h/24*(9*f(t[i+1],w[2,i+1])+19*f(t[i],w[1,i])-5*f(t[i-1],w[1,i-1])+f(t[i-2],w[1,i-2])   )
        w[4,i+1]=w[1,i]+h/24*(9*f(t[i+1],w[3,i+1])+19*f(t[i],w[1,i])-5*f(t[i-1],w[1,i-1])+f(t[i-2],w[1,i-2])   )
        k=k+0.1
    for i in range(0,21,5):
        print("%.1f & %.8f & %.8f & %.8f & %.8f & %.8f\\\\" %(i/10,y(i/10),w[1,i],w[2,i],w[3,i],w[4,i]) )
    print()
    for i in range(0,21,5):
        print("%.1f & %.8f  & %.8f & %.8f  & %.8f \\\\" %(i/10,abs(y(i/10)-w[1,i]),abs(y(i/10)-w[2,i]),abs(y(i/10)-w[3,i]),abs(y(i/10)-w[4,i])))

Adams_FourthOrder(0,2,20,-2)
