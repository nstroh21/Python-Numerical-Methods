
# try implementing the CORDIC algorithm
# Calculate sin and cos, all other trig functions can be gotten from this
#inverse functions don't know yet
# we only need to calculate on interval 0 to pi/2
# Example Sine structure
#pi is needed, calculate pi to some accuray

import math
from common import abs, round
from NewtonNthRoot import sqRoot

#globals
pi = math.pi
tolerance = 10**(-18)
tan_table = [math.atan(2**(-i)) for i in range(0,55)]

def sin(x): #type = ["rad", "deg"]):
    # convert x to be somewhere on the unit circle first
    # this is maybe achieved finding x mod(2*pi) 
    if (x > 0) & (x <= pi/2):
        return round(cordic(x)[1],15)
    elif (x > pi/2) & (x < pi):
        # recursion with transformation
        return sin(pi/2 - x)
    elif (x > pi) & (x < 3*pi/2):
        return -1*sin(x-pi)
    else: return -1*sin(2*pi - x)

def cos(x):
    # convert x to be somewhere on the unit circle first
    # this is maybe achieved finding x mod(2*pi) 
    if (x > 0) & (x < pi/2):
        return round(cordic(x)[0],15)
    elif (x > pi/2) & (x < pi):
        # recursion with transformation
        return round(-1*cos(pi-x),18)
    elif (x > pi) & (x <= 3*pi/2):
        return round(-1*cos(x-pi),18)
    else: return round(1*cos(2*pi -x),18)

def tan(x): 
    return sin(x)/cos(x)

def csc(x):
    return 1/sin(x)

def sec(x):
    return 1/cos(x)

def cot(x):
    return cos(x)/sin(x)

def cordic(alpha):
    # some fun stuff to get trig approxminations for cos, sin
    # 50 values of tangent since that is about how much is needed for decent accuracy according to wikipedia
    #pretend like it's hardcoded, really just going to use a list 
    theta = 0
    x = 1
    y = 0
    A = 1
    d = 1
    # this is not converging that's why my code keeps getting stuck in infinite loops
    # make a for loop to see whats happening
    for iteration in range(0,55):
        if (abs(alpha-theta) <= tolerance):
            break
        A = 1/math.sqrt((1+2**(-2*iteration)))
        if (alpha > theta): 
            d = 1
        else: 
            d = -1
        # the following stpe could also be done as a matrix multiplication
        x1 = A*( x - y*d*(2**(-iteration)) )
        y1 = A*( x*d*(2**(-iteration)) + y )
        x = x1
        y = y1
        theta = theta + d*(tan_table[iteration])

    return x, y, iteration, theta