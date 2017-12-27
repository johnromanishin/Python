# Problem Set 3
# Name: John Romanishin
# Collaborators:
# Time: 


# Assume eGrowth can take values in the range [-100.0, 100.0].

def futureEndowment (n, eInit, tInit, eGrowth, tGrowth, subsidy, y):


    currente = (eInit - n*tInit*subsidy/100.0)*(1 + (eGrowth/100.0))
    currentt = (tInit*(1+ (tGrowth/100.00)))
    #print (currente)
    #print y
    newy = y - 1
    if newy == 0:
        return currente
    final = futureEndowment(n, currente, currentt, eGrowth, tGrowth, subsidy, newy)
    return final






def findMinEndowmentGrowth(n, eInit, tInit, tGrowth, subsidy, y, epsilon): # This is going to create a function to find the minimum possible egrowth value where the final value of the endowment
# is zero after y years

    guess = 0 # This creates a variable, guess, this will be what we will play with to find
    guessmax = 100.0
    guessmin = -100.0
    iteration = 0.0
    currentEndowment = futureEndowment (n, eInit, tInit, guess, tGrowth, subsidy, y)
    print currentEndowment
    while ((-1)*epsilon > currentEndowment or currentEndowment > epsilon):
        currentEndowment = futureEndowment (n, eInit, tInit, guess, tGrowth, subsidy, y)
        while currentEndowment < guess:
            print currentEndowment
            iteration = iteration + 1.0
            guess = (guess + (guessmax / (2.0*iteration)))
            currentEndowment = futureEndowment (n, eInit, tInit, guess, tGrowth, subsidy, y)
            break
        
        while currentEndowment > guess:
            print currentEndowment
            iteration = iteration + 1.0
            guess = (guess + (guessmin / (2.0*iteration)))
            currentEndowment = futureEndowment (n, eInit, tInit, guess, tGrowth, subsidy, y)
            break
    print currentEndowment
    print guess
    egrowth = guess
    return egrowth
        




findMinEndowmentGrowth(10, 1000, 100, 10, 30, 10, 5)
print "the real deal foo"
