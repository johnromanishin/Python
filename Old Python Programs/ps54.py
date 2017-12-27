# Problem set 2
# Name: John Romanishin
# Collabortors: R Tharu
# Time: 6:00

# Enumerate possible answers starting at 1 McNugget
# For each possible answer n,
#    Check if there exists x, y, and z such that 6x+9y+20z = n
#        (this can be done by looking at all feasible combinations of x, y, and z)
#    If not, n is a possible answer, save n
#    When you have found six consecutive values of n that have solutions,
#        the last answer that was saved is the correct answer
#
# Problem 3.
#
# Write an iterative program that finds the largest number of McNuggets it is not possible to buy.
#
# Hint: Your program should follow the outline above.
# 20 McNuggets. So, for example, it is possible to buy 15 McNuggets
# (with one package of 6 and one package of 9), but not 16 McNuggetsn
# x = 0
# y = 0
# z = 0

def ispossible(n):
    for x in range(0,n):
        for y in range(0,n):
            for z in range(0,n):
                if 6*x + 9*y + 20*z == n:
                    return True
    return False
# above is the definition of a checking function
count = 0
a = True
n = 1
while count < 6:
    test = ispossible(n)
    if test == True:
        count = count+1
    elif test == False:
        count = 0
    n = n+1
print "largest number of McNuggets it is not possible to buy =",(n-7)
        
