def abs(x):
    if (x < 0):
        return x*-1
    else:
        return x

# recursion limit is apparently less than 10 so this should be iterative instead
#how do I change that ?
def pow(x, n):
    y = 1
    for i in range(0,abs(n)):
        y = x*y
    if (n < 0):
        return 1/y
    else:
        return y

def truncate(x, places):
    if places < 0:
        print("Places must be a positive integer")
        return
    y = x*(pow(10, places))
    truncy = int(y)
    newx = truncy / (pow(10,places))
    return newx

def round(x,n):   
    y = x*(10**(n+1))
    if(y%10 >= 5):
        y = y + 10 - (y%10)
        truncy = int(y)
        newx = truncy/(10**(n+1))
    else:
        newx = truncate(x, n)
    return newx

