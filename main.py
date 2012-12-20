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

# All directions a Queen can capture on.
SLOPES = [1, -1, 0, None]

class Queens(object):
    
    def __init__(self):
        self.board = self.__board()
    
    def __ispositive(self, num):
        '''Determine if a number is positive'''
        if int(num) >= 0:
            return True
        else:
            return False
        
    def __board(self):
        '''Create a empty board'''
        board = {}
        for x in range(0, 8):
            board[x] = {}
            for y in range(0, 8):
                board[x][y] = None
        return board
    
    def __placed(self):
        '''Get current placed queens'''
        return [ (x, y) for x in self.board for y in self.board[x] if self.board[x][y] ]
                
    def __captures(self, slope, x, y):
        '''Get a list of all x,y coords for captures'''
        if slope != None:
            yintercept = y - (slope * x)
            captures = []
            for xkill in range(0, 8):
                ykill = (slope * xkill) + yintercept
                if self.__ispositive(xkill) and self.__ispositive(ykill):
                    captures.append((xkill, ykill))
            return captures
        else:
            return [ (x, i) for i in range(0, 8) ]
        
    def getQueens(self, start=0):
        '''Place as many uncapturable Queens as possible'''
        self.board = self.__board()
        spots = [ (x, y) for x in self.board for y in self.board[x] ]
        
        # used to hold our Queens capture spots
        captures = []
        
        # loop over all our spots starting with start
        while spots:
            try:
                x, y = spots.pop(start)
            except IndexError:
                x, y = spots.pop(0)
            
            # used to hold spots the Queen can capture from a spot
            spot_captures = []
            
            # be sure spot isn't already taken
            if not self.board[x][y]:
                
                # build a capture list
                for slope in SLOPES:
                    spot_captures += self.__captures(slope, x, y)
                
                # if the queen is uncapturable from here place it
                if (x,y) not in captures:
                    self.board[x][y] = True
                    captures += spot_captures
        
        # return where all Queens are for this board state
        return self.__placed()

def main():
    q = Queens()
    for i in range(0, 64):
        res = q.getQueens(start=i)
        print 'Starting at position %s we have %s uncapturable Queens: \n%s\n' % \
                (i, len(res), res)
        
if __name__ == '__main__':
    main()
