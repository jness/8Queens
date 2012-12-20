#!/usr/bin/env python
#
# Written by Jeffrey Ness
#
# A solution to the 8 Queens problem commonely asked
# to software developers where 8 Queens need to be placed
# but no Queen can capture another Queen.
#
# My solution uses 4 line slopes one for each
# direction a queen can travel, and a line equation
# to determine all spots a queen can capture on.
#

from itertools import permutations

class Queens(object):
    
    def __init__(self):
        pass
    
    def __ispositive(self, num):
        '''Determine if a number is positive'''
        if int(num) >= 0:
            return True
        else:
            return False
            
    def __points(self, pos):
        '''Get all points a Queen can capture'''
        spots = []
        x, y = pos
        for slope in [1, -1]:
            b = y - (slope * x)
            for xkill in range(8):
                ykill = (slope * xkill) + b
                if self.__ispositive(xkill) and self.__ispositive(ykill):
                    if (xkill, ykill) != pos:
                        spots.append((xkill, ykill))
        return spots
    
    def solutions(self):
        '''Get all solutions'''
        solutions = []
        cur = permutations(range(8))
        for s in cur:
            captures = []
            vals = [ i for i in enumerate(s) ]
            for val in vals:
                captures += self.__points(val)
            
            res = [ True for v in vals if v in captures ]
            if not res:
                solutions.append(vals)
        
        return solutions
                
def main():
    q = Queens()
    solutions = q.solutions()
    for s in solutions:
        print s
    
if __name__ == '__main__':
    main()