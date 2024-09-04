

from operator import floordiv, mod

def divide_exact(n, d):
    """our first python source file."""
    """Return the quotient and remainder of dividing N by D.
    >>> q,r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
   
    return floordiv(n, d), mod(n, d)

q, r = divide_exact(2013, 10)
print('Quotient:', q)
print('Remainder:', r)

def absolute_value(x):
    if x <0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
    
