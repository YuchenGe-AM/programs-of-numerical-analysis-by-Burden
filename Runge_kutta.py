import math
import numpy as np
from sympy import *
from matplotlib import pyplot as plt
# Runge-Kutta's method
def f(t,y):
    return -(y+1)*(y+3)
def y(t):
    return -3+2*(1+math.exp(-2*t))**(-1)
def Runge_Kutta(a,b,N,alpha):
    h=(b-a)/N
    t=a
    w=alpha
    k=0
    for i in range(1,N+1):
        K1=h*f(t,w)
        K2=h*f(t+h/2,w+K1/2)
        K3=h*f(t+h/2,w+K2/2)
        K4=h*f(t+h,w+K3)
        w=w+(K1+2*K2+2*K3+K4)/6
        t=a+i*h
        k=k+0.2
        print("%.1f & %.8f & %.8f\\\\" %(k,w,abs(w-y(t))) )
def hermite(p,x, y, dy):
    f = 0
    n = len(x)
    for i in range(n):
        la = 1
        lp = 0
        for j in range(n):
            if j != i:
                la = la*(p - x[j])/(x[i] - x[j])
                lp = lp + 1/(x[i] - x[j])
        temp1 = 1 - 2 * (p - x[i])*lp
        temp2 = y[i] * temp1 * la * la
        temp3 = dy[i] * (p - x[i]) * la * la
        f = f + temp2 + temp3
    return f
Runge_Kutta(0,2,20,-2)
# interpolation approximation 
y1=hermite(1.3,[1.2,1.4],[-1.16637354,-1.11467694],[f(1.2,-1.16637354),f(1.4,-1.11467694)])
y2=hermite(1.93,[1.8,2],[-1.05321755,-1.03599222],[f(1.2,-1.05321755),f(1.4,-1.03599222)])
print()
print('The result y(1.3) applying Runge_Kutta method with h=0.2 is %.8f with error %.8f' %(y1,y(1.3)-y1)  )
print('The result y(1.93) applying Runge_Kutta method with h=0.2 is %.8f with error %.8f' %(y2,y(1.93)-y2)  )