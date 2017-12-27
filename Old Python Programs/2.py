class Person: 
    def __init__(self, family_name, first_name): 
        self.family_name = family_name 
        self.first_name = first_name 
    def familyName(self): 
        return self.family_name 
    def firstName(self): 
        return self.first_name 
    def __cmp__(self, other): 
        return cmp(self.family_name+self.first_name, 
                   other.family_name+other.first_name) 
    def __str__(self): 
        return '<Person: %s %s>'%(self.first_name, self.family_name) 
class MITPerson(Person): 
    nextIdNum = 0 
    def __init__(self, family_name, first_name): 
        self.family_name = family_name 
        self.first_name = first_name 
        self.idNum = MITPerson.nextIdNum 
        MITPerson.nextIdNum += 1 
    def getIdNum(self): 
        return self.idNum 
    def __str__(self): 
        return '<MIT Person: %s %s>'%(self.first_name, self.family_name) 
class UG(MITPerson): 
    """year is an integer between 1 and 7""" 
    def setYear(self, year): 
        self.year = year 
    def __str__(self): 
        return '<UG: %s %s>'%(self.first_name, self.family_name) 
p1 = Person('Smith', 'Mary') 
p3 = UG('Clemens', 'Roger')
p2 = UG('Schilling', 'Curt') 
print p1>p2
print p1.getIdNum( )

