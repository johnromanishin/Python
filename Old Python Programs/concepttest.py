import math
"""
def complexPolar(p):
    """
    #@param p: int, float, or complex number
    #@returns: polar representation as a pair of r, theta
    """
    if isinstance(p, complex):
        return (abs(p), math.atan2(p.imag, p.real))
    elif p >= 0:
        return (p, 0.0)
    else:
        return (abs(p), math.pi)

print complexPolar(0 +1j)[0]
"""
