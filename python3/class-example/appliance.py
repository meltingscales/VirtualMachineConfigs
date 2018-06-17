total = 0

class Appliance:
    name = None
    cost = None
    usage = None
  
    def __init__(self, n, c, u):
        self.name = n
        self.cost = float(c)
        self.usage = float(u)
    
    def __str__(self): # When we call `str` on self.
      return str(self.name) + " costs " + str(self.cost * self.usage) + " dollars"
	
    def __repr__(self): # When object gets printed with `print`.
      return str(self)
    
def appl():
    """Generate an Appliance object from user input."""
    global total
    name = input("Enter the appliace name:  ")
    cost = input("Enter the cost per KW: ")
    usage =input("Enter the annual usage in hours: ")
    annual = (float(cost)) * (float(usage))
    total = float(cost)  + float(total)
    x = Appliance(name, cost, usage)
    return x

  
if __name__ == '__main__':
    
    x = 0
    
    while(x >= 0):
        x = int(input("Give me a negative number."))
        
        if(x >= 0):
            print("that ain't negative!")
        else:
            print("thx!")
    
    a1 = appl()
    print(a1)
