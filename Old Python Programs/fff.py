class Thing:
   def set(self, v):
      self.x = v
   def get(self):
      return self.x
   def mangle(self):
      print "what the FUck$$"
      self.set(4)#(self.get+1)
      print "what the fuck"
      self.hasBeenMangled = True
      return self.get
    
print 'yomama'
a = Thing()
a.set(3)
print a.get()
print a.mangle()
print a.get()
print a.get()
print a.hasBeenMangled
