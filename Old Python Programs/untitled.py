class Polynomial:
    def __init__(self, coefficients):
        self.coeffs = coefficients
        self.length = len(coefficients)
    def coeff(self, i):
        return self.coeffs[-i]

    def add(self, other):
        #print "STARTING ADDING PROCEDURE"
        newcoeff = []
        selfcoeff = self.coeffs[:] # copies list so that original list is unchanged
        othercoeff = other.coeffs[:] # copies list so that original list is unchanged
        while len(othercoeff) != len(selfcoeff):
            if self.length < other.length:
                selfcoeff = [0] + selfcoeff 
                #print str(selfcoeff)
            else:
                othercoeff = [0] + othercoeff 
                #print str(othercoeff)
        #print "OUT OF LOOP"
        for item in range(len(selfcoeff)):
            newcoeff = newcoeff + [(selfcoeff[item]+othercoeff[item])]
        #print str(Polynomial(newcoeff))
        return Polynomial(newcoeff)
        

    def mul(self, other):
        #print "IN MULTIPLY"
        biglist = []
        coefflist = []
        newcoeff = []
        selfcoeffs = self.coeffs[:] # copies list so that original list is unchanged
        othercoeffs = other.coeffs[:] # copies list so that original list is unchanged
        selfcoeffs.reverse()
        othercoeffs.reverse()
        #print str(selfcoeffs)
        #print str(othercoeffs)
        for i in range(len(othercoeffs)):
            #print str(i)
            for item in range(len(selfcoeffs)):
                #print str(item)
                #print "MADE IT HERE"
                z = selfcoeffs[item]*othercoeffs[i]
                #print str(z)
                biglist.append([(i+item), z])
                coefflist.append(i+item)
        #print biglist
        #print max(coefflist)
        newcoeff = [0]*(max(coefflist)+1)
        #print range(0,max(coefflist)+1)
        for index in range(0,max(coefflist)+1):
            #print "in bigloop"
            #print str(index)
            for mini in biglist:
                #print str(mini)
                if mini[0] == index:
                    newcoeff[index] = newcoeff[index] + mini[1]
        #print "HERE"
        newcoeff.reverse()
        #print str(newcoeff)
        return Polynomial(newcoeff)
       
        
        
    def __str__(self):
        return str(self.coeffs)
    
    def val(self, v):
        total = 0
        listt = range(len(self.coeffs))
        print "listt",listt
        coeffss = self.coeffs[:]
        print self.coeffs
        coeffss.reverse()
        print "coeffss",coeffss
        for indexx in listt:
            total = total + coeffss[indexx]*(v**indexx)
            print "total = ",+ total
            print "times v**index", (v**indexx), "=", total
        return total
            
   
            
        
    def roots(self):
        rootlist = []
        if self.length > 3:
            return "error, ERROR"

        root1 = (((-1)*(self.coeffs[1]+0j) + ((self.coeffs[1]+0j)**2 - 4*(self.coeffs[0]+0j)*(self.coeffs[2]+0j))**(0.5))/(2*(self.coeffs[0]+0j)))
        rootlist.append(root1)
        root2 = (((-1)*(self.coeffs[1]+0j) - ((self.coeffs[1]+0j)**2 - 4*(self.coeffs[0]+0j)*(self.coeffs[2]+0j))**(0.5))/(2*(self.coeffs[0]+0j)))
        rootlist.append(root2)
        print rootlist
        return rootlist
        

    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)
    def __call__(self,x):
        return self.val(x)
    def __repr__(self):
        return str(self)
p1 = Polynomial([1,2,3])
