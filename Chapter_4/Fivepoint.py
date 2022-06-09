# method of five-point midpoint(endpoint) formula
# midpoint version
def Fivepointmid(a,b,c,d,h):
    Y=(a-8*b+8*c-d)/(12*h)
    return Y
# left endpoint version
def Fivepointendleft(a,b,c,d,e,h):
    Y=(-25*a+48*b-36*c+16*d-3*e)/(12*h)
    return Y
# right endpoint version
def Fivepointendright(a,b,c,d,e,h):
    Y=(-3*a+16*b-36*c+48*d-25*e)/(12*h)
    return Y


print('The approximation for derivative at x=2.1 is', Fivepointendleft(-1.709847,-1.373823,-1.119214,-0.9160143,-0.7470223,0.1),'.')
print('The approximation for derivative at x=2.2 is', Fivepointendleft(-1.373823,-1.119214,-0.9160143,-0.7470223,-0.6015966,0.1),'.')
print('The approximation for derivative at x=2.3 is', Fivepointmid(-1.709847,-1.373823,-0.9160143,-0.7470223,0.1),'.')
print('The approximation for derivative at x=2.4 is', Fivepointmid(-1.373823,-1.119214,-0.7470223,-0.6015966,0.1),'.')
print('The approximation for derivative at x=2.5 is', Fivepointendright(-1.709847,-1.373823,-1.119214,-0.9160143,-0.7470223,0.1),'.')
print('The approximation for derivative at x=2.6 is', Fivepointendright(-1.373823,-1.119214,-0.9160143,-0.7470223,-0.6015966,0.1),'.')