import math
import numpy as np
from sympy import *
from matplotlib import pyplot as plt
# initialization
w=[0.5,0.5,0.5,0.5]
k=[[0.5]*5 for i in '12345']
k=np.matrix(k)
def y(t):
    return 43/36*math.exp(t)+1/4*math.exp(-t)-4/9*math.exp(-2*t)+1/6*t*math.exp(t)
def f1(t,w1,w2,w3):
    return w2
def f2(t,w1,w2,w3):
    return w3
def f3(t,w1,w2,w3):
    return 2*w1+w2-2*w3+math.exp(t)
# Runge-Kutta Method for Systems of Differential Equations
def Runge_Kutta_Systems(a,b,N,alpha):
    h=(b-a)/N 
    t=a
    for j in range(1,4):
        w[j]=alpha[j]
    print("%.1f & %.8f & %.8f & %.8f & %.8f & %.8f\\\\" %(t,y(t),w[1],abs(y(t)-w[1]),w[2],w[3]) )
    for i in range(1,N+1):
        # 1
        k[1,1]=h*f1(t,w[1],w[2],w[3])
        k[1,2]=h*f2(t,w[1],w[2],w[3])
        k[1,3]=h*f3(t,w[1],w[2],w[3])
        # 2
        k[2,1]=h*f1(t+h/2,w[1]+k[1,1]/2,w[2]+k[1,2]/2,w[3]+k[1,3]/2)
        k[2,2]=h*f2(t+h/2,w[1]+k[1,1]/2,w[2]+k[1,2]/2,w[3]+k[1,3]/2)
        k[2,3]=h*f3(t+h/2,w[1]+k[1,1]/2,w[2]+k[1,2]/2,w[3]+k[1,3]/2)
        # 3
        k[3,1]=h*f1(t+h/2,w[1]+k[2,1]/2,w[2]+k[2,2]/2,w[3]+k[2,3]/2)
        k[3,2]=h*f2(t+h/2,w[1]+k[2,1]/2,w[2]+k[2,2]/2,w[3]+k[2,3]/2)
        k[3,3]=h*f3(t+h/2,w[1]+k[2,1]/2,w[2]+k[2,2]/2,w[3]+k[2,3]/2)
        # 4
        k[4,1]=h*f1(t+h,w[1]+k[3,1],w[2]+k[3,2],w[3]+k[3,3])
        k[4,2]=h*f2(t+h,w[1]+k[3,1],w[2]+k[3,2],w[3]+k[3,3])
        k[4,3]=h*f3(t+h,w[1]+k[3,1],w[2]+k[3,2],w[3]+k[3,3])
        for j in range(1,4):
            w[j]=w[j]+(k[1,j]+2*k[2,j]+2*k[3,j]+k[4,j])/6
        t=a+i*h 
        print("%.1f & %.8f & %.8f & %.8f & %.8f & %.8f\\\\" %(t,y(t),w[1],abs(y(t)-w[1]),w[2],w[3]) )
Runge_Kutta_Systems(0,3,15,[0,1,2,0])




