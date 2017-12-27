# Problem set 2b
# Name: John Romanishin
# Collabortors: David Crowl
# time: 4:00
# This is one day late. I wish to use one of my late days for this. 




def canBuy(n, packages): # Creates a function that can be used in further programs
    "Returns true if that number of nuggets can be purchased" # this is what it tells the programmer when he tries to use the program
    for testrun in range(0, n/packages[-1]+1):
        if (testrun*packages[-1] == n):
            return True
        elif packages[0]!= packages[-1]:
            if canBuy(n-packages[-1]*testrun,packages[0:-1])==False:
                continue
            if canBuy(n-packages[-1]*testrun,packages[0:-1])==True:
                return True
        else:
            if packages[0] == packages[-1]:
                continue
    return False

## Below is what I downloaded from the website

def findMax(packages):
    smallestPackage = packages[0]
    nuggets = 1
    consecYes = 0
    largest = None

    while consecYes < smallestPackage:
        if canBuy(nuggets, packages): 
            consecYes += 1
        else:
            consecYes = 0
            largest = nuggets
        if nuggets >= 150:
            break
        nuggets += 1

    if largest != None:
        print 'The largest number of McNuggets <= 150 one cannot buy is', largest
    else: 
        print 'It is possible to buy all numbers up to 150.'

packages = (6, 9, 20)
findMax(50)
