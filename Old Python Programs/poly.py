class Polynomial:
    
    def __init__(self, coefficients):
        self.coeffs = coefficients
        self.len = len(coefficients)

    def __str__(self):
        print self.coeffs[0], 'x^4  ',  self.coeffs[1], 'x^3  ',  self.coeffs[2],'x^2  ',  self.coeffs[3],'x^1  ',  self.coeffs[4],'x^0'

    def __add__(self, other):
        return self.add(other)

    def __call__(self, x):
        return self.val(x)
        

    def mul(self, other):
        pass
    
    def add(self, other):
        while len(self.coeffs) != len(other):
            if self.len < len(other):
                
                self.coeffs = [0] + self.coeffs
                #print self.coeffs
            else:
                other = [0] + other
        print self.coeffs," Other", other
        new = [0,0,0,0]
        for x in range(len(self.coeffs)):
            #print x,
            new[x] = (self.coeffs[x] + other[x])
        print new
        return new

    def val(self, v):
        pass

    def roots(self):
        pass
    #__repr__ = __str__

    
    
#print "hi"

#x = Polynomial([1,10,100])

#print "x is created"
#print x.add([4,5,6,4])

#print x
