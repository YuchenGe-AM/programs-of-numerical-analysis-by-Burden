import math
import numpy as np
r=[[0]*6,[0]*6,[0,0.5773502692,-0.5773502692,0,0,0],[0,0.7745966692,0,-0.7745966692,0,0],[0,0.8611363116,0.3399810436,-0.3399810436,-0.8611363116,0],[0]*6]
c=[[0]*6,[0]*6,[0,1,1,0,0,0],[0,0.5555555556,0.8888888889,0.5555555556,0,0],[0,0.3478548451,0.6521451549,0.6521451549,0.3478548451,0],[0]*6]
r=np.mat(r)
c=np.mat(c)
Real=(math.exp(0.5)-1)*(1-math.exp(-0.5))
def f(x,y):
	return math.exp(y-x)
# method of gaussian double integration
def Gaussiandouble(m,n):
	h1=0.5/2
	h2=0.5/2
	k1=0.5/2
	k2=0.5/2
	J=0
	for i in range(1,m+1):
		JX=0
		x=h1*r[m,i]+h2
		for j in range(1,n+1):
			y=k1*r[n,j]+k2
			Q=f(x,y)
			JX=JX+c[n,j]*Q
		J=J+c[m,i]*k1*JX
	return h1*J
# method of 3-point gaussLegendre double integration
def Simpson(m,n):
	h=0.5/n
	J1=0
	J2=0
	J3=0
	for i in range (0,n+1):
		x=0+i*h
		HX=0.5/m
		K1=f(x,0)+f(x,0.5)
		K2=0
		K3=0
		for j in range (1,m):
			y=0+j*HX
			Q=f(x,y)
			if j/2==0:
				K2=K2+Q
			else:
				K3=K3+Q
		L=(K1+2*K2+4*K3)*HX/3
		if i==0 or i==n:
			J1=J1+L 
		elif i/2==0:
			J2=J2+L 
		else:
			J3=J3+L 
	J=h*(J1+2*J2+4*J3)/3
	return J
print('Approximation with Simpson by n=m=4 is',Simpson(4,4),'with error term',abs(Real-Simpson(4,4)))
print('Approximation with GaussianLegendre by n=m=3 is',Gaussiandouble(3,3),'with error term',abs(Real-Gaussiandouble(3,3)))
