def argmin(f, input):
    bestValSoFar = None
    bestArgSoFar = None
    y = 0
    for x in input:
        z = f(x)
        if y == 0:
            bestValSoFar = z
            bestArgSoFar = x
            y = 1
        elif z < bestValSoFar:
            bestValSoFar = z
            bestArgSoFar = x
        else:
            pass
    return(bestValSoFar,bestArgSoFar)
print argmin(lambda x: (x-3)**2, [1,2,3,4])
