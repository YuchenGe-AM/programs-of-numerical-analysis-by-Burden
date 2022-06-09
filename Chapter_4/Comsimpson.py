import math
pi=math.pi
Real=(3+math.exp(4)*(2*math.sin(6)-3*math.cos(6)))/13  

# method of composite trapezoidal
def trapezoidal(a,b,n):
    h=(b-a)/n
    XI=[math.exp(4)*math.sin(6),0,0]
    for i in range(1,n): # different from python! Note that Python starts from 0.
        X=a+i*h
        XI[1]=XI[1]+math.exp(2*X)*math.sin(3*X)
    Y=h*(XI[0]+2*XI[1])/2
    return  Y

# method of composite simposon
def Simpson(a,b,n):
    h=(b-a)/n
    XI=[math.exp(4)*math.sin(6),0,0]
    for i in range(1,n): # different from python! Note that Python starts from 0.
        X=a+i*h
        if i%2==0:
            XI[2]=XI[2]+math.exp(2*X)*math.sin(3*X)
        else:
            XI[1]=XI[1]+math.exp(2*X)*math.sin(3*X)
    Y=h*(XI[0]+4*XI[1]+2*XI[2])/3
    return  Y

# method of composite midpoint
def Midpoint(a,b,n):
    h=(b-a)/(n+2)
    XI=math.exp(4)*math.sin(6)
    for i in range(1,n/2+1): # different from python! Note that Python starts from 0.
        X=a+i*h
        XI=XI+math.exp(2*X)*math.sin(3*X)
    Y=2*h*XI
    return  Y


print('The real value is', Real)
print('Approximation with composite trapezoidal rule by n=2169 is', Real-trapezoidal(0,2,2169))
print('Approximation with composite simposon rule by n=54 is', Real-Simpson(0,2,54))
print('Approximation with composite midpoint rule by n=3067 is', Real-Simpson(0,2,3067))

