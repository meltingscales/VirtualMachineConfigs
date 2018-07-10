import copy
from collections import deque

def nidx(idx, lst):

    if(idx < 0): # too small
        return nidx(idx + len(lst), lst)
    if(idx >= len(lst)): # too large
        return nidx(idx - len(lst), lst)
    return idx

class CellularAutomaton(object):


    grid = [ #2d list
        deque(['0' for i in range(25)]),
        ]

    grid[0][len(grid[0])//2] = '1' # first row has a single black in middle.
    
    colors = 2
    width = 3

    rules = {
    '000': '0',
    '001': '1',
    '010': '1',
    '011': '1',
    '100': '1',
    '101': '0',
    '110': '0',
    '111': '0'
    }

    def cycle(self, times=1):
        
        if(times <= 0):
            return
        
        row = self.grid[-1] # get last row
        newrow = deque() # blank row
        
        print(f"ROW {len(self.grid)}:")
        print(''.join(row))

        for i in range(len(row)): # loop though all cells

            lb = -((self.width//2))
            ub = -lb
            
            lb += i
            ub += i 
            #Upper and lower bounds. the 'key' for rules.

            rule = ''
            for i in range(lb, ub+1, 1):
                rule += row[nidx(i, row)]

            newrow.append(self.rules[rule])
            
            print(f"{nidx(lb, row):2d} - {nidx(ub, row):2d}: {rule} -> {self.rules[rule]}")

        self.grid.append(newrow)

        self.cycle(times-1)

    def __init__(self):
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        return '\n'.join(
            [''.join(row) for row in self.grid]
            )


ca = CellularAutomaton()

ca.cycle()

print(ca)
