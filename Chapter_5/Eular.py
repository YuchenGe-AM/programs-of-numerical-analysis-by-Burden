import math
Real=math.exp(-5)+5
# eular's method
def f(t,y):
    return -y+t+1
def eular(a,b,N,alpha):
    h=(b-a)/N
    t=a
    w=alpha
    for i in range(1,N+1):
        w=w+h*f(t,w)
        t=a+i*h
    return w
print('The result applying Eular method with h=0.2 is',eular(0,5,25,1),'with error',Real-eular(0,5,25,1))
print('The result applying Eular method with h=0.1 is',eular(0,5,50,1),'with error',Real-eular(0,5,50,1))
print('The result applying Eular method with h=0.05 is',eular(0,5,100,1),'with error',Real-eular(0,5,100,1))
print('The result applying Eular method with h=0.0014 is',eular(0,5,3535,1),'with error',Real-eular(0,5,3535,1))
