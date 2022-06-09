import math
# Modified_Eular's method
def f(t,y):
    return y-t**2+1
def y(t):
    return (t+1)**2-0.5*math.exp(t)
def Modified_Eular(a,b,N,alpha):
    h=(b-a)/N
    t=a
    w=alpha
    for i in range(1,N+1):
        w=w+h*f(t,w)
        t=a+i*h
        print(w,'&',y(t)-w)
def interpolation(t,a,b,c,d):
    return (d-c)/(b-a)*(t-a)+c
Modified_Eular(0,2,10,0.5)
# interpolation approximation 
y1=interpolation(1.3,1.2,1.4,-1.172210612839059,-1.1200763302151344)
y2=interpolation(1.93,1.8,2,-1.0571698907180425,-1.0391938189655483)
print()
print('The result y(1.3) applying Modified_Eular method with h=0.2 is',y1,'with error',y(1.3)-y1)
print('The result y(1.93) applying Modified_Eular method with h=0.2 is',y2,'with error',y(1.93)-y2)