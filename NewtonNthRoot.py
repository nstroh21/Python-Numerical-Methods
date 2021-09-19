# define several functions -- Netwon-Raphson's Method "newtRaph()"
# use this to create a square root calculator
# generalize to n-root calculator
from common import abs, pow, truncate

fx = lambda x,n, N: x**n - N
fPrime = lambda x, n: n*(x**(n-1))

def newtRaphRoot(n, N, maxIters = 100, accuracy = 10):
    tol = pow(10, (-1 * accuracy))
    #x1 is the initial guess
    x1 = N/(n**2) # no real reason right now excpet guess and check it felt like a decent first guess
    for iteration in range(1, maxIters):
        x2 = x1 - (fx(x1, n, N) / fPrime(x1, n))
        # check if tolerance level is met if yes then exit the loop
        if (abs(fx(x2, n, N)) < tol):
            break
        else:
            x1 = x2
    return x2, iteration, N/n**2, fx(x2, n, N)

def nRoot(radicand, n):
    if (n == 1):
        return radicand
    else:
        est = newtRaphRoot(n, radicand, accuracy = 6)[0]
        if (truncate(est, 4) - int(est) == 0.0000):
            return truncate(est,1)
        else: 
            return est
    # etc. start this tomorrows

def sqRoot(radicand):
    return nRoot(radicand,2)