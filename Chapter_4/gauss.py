import math
import numpy as np
e=math.exp(1)
Real=2-5/e
def g(x):
    return 1/2*(((x+1)/2)**2)*math.exp(-(x+1)/2)
# input the number of points 
def Gauss(n):
    if n==2:
        return g(0.5773502692)+g(-0.5773502692)
    if n==3:
        return 0.5555555556*g(0.7745966692)+0.8888888889*g(0)+0.5555555556*g(-0.7745966692)
    if n==4:
        return 0.3478548451*(g(0.8611363116)+g(-0.8611363116))+0.6521451549*(
            g(0.3399810436)+g(-0.3399810436))
    if n==5:
        return 0.2369268850*(g(0.9061798459)+g(-0.9061798459))+0.5688888889*g(0)+0.4786286705*(
            g(0.5384693101)+g(-0.5384693101))
print("The approximation applying 2-point gauss quadrature is", Gauss(2), "with error term",abs(Real-Gauss(2)))
print("The approximation applying 3-point gauss quadrature is", Gauss(3), "with error term",abs(Real-Gauss(3)))
print("The approximation applying 4-point gauss quadrature is", Gauss(4), "with error term",abs(Real-Gauss(4)))
print("The approximation applying 5-point gauss quadrature is", Gauss(5), "with error term",abs(Real-Gauss(5)))