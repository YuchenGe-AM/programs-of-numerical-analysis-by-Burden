import math
# Heun's method
def f(t,y):
    return -(y+1)*(y+3)
def y(t):
    return -3+2*(1+math.exp(-2*t))**(-1)
def Heun(a,b,N,alpha):
    h=(b-a)/N
    t=a
    w=alpha
    k=0
    for i in range(1,N+1):
        w=w+h/4*(f(t,w)+3*f(t+2/3*h,w+2/3*h*f(t,w)))
        t=a+i*h
        k=k+0.2
        print("%.1f & %.8f & %.8f\\\\" %(k,w,abs(w-y(t))) )
def interpolation(t,a,b,c,d):
    return (d-c)/(b-a)*(t-a)+c
Heun(0,2,10,-2)
# interpolation approximation 
y1=interpolation(1.3,1.2,1.4,-1.1699932308872074,-1.1183617793290332)
y2=interpolation(1.93,1.8,2,-1.0562505811390515,-1.0391938189655483)
print()
print('The result y(1.3) applying Heun method with h=0.2 is %.8f with error %.8f' %(y1,y(1.3)-y1)  )
print('The result y(1.93) applying Heun method with h=0.2 is %.8f with error %.8f' %(y2,y(1.93)-y2)  )