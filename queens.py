# N queens
# Andy Tien
import collections, copy

class Position:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def compare(self, other_position):
        assert isinstance(other_position, Position)
        return self.x == other_position.x and self.y == other_position.y


class Board:
    def __init__(self, n):
        self.valid_positions = []
        self.queens_left = n
        self.size = n
    def _placeQueen(valid_positions, queen_position, boardsize):
        #Given the list of valid positions, the position we want to place the queen, 
        #and the boardsize, return a new list of positions that would be invalidated
        pass
        
    def solve(self):
        for positions in self.valid_positions:
            print positions

        # Perhaps this can be solved recrusively? Repeatly call self with valid_positions and
        # queens left to place.

def makeBoard(n):
    """ Builds a board of size n """
    valid_positions = []
    for i in range(0, n):
        for j in range(0,n):
            valid_positions.append(Position(i,j))
    return valid_positions

def validatePosition(boardsize, pos):
    """ Check to see if the position is a valid position on the board
    """
    return pos.x in range(0, boardsize) and pos.y in range(0,boardsize)

def generateQueenAttacks(boardsize, pos):
    """ Generates a list of all positions that the Queen can attack.
    """
    assert isinstance(pos, Position) and validatePosition(boardsize, pos)
    #pos = (x, y)
    attackList = []
    startPos = Position(pos.x, pos.y)
    
    def addAttackList(pos):
        for attacked in attackList:
            if pos.compare(attacked):
                return
        attackList.append(Position(pos.x, pos.y))

    #positive x
    while pos.x < boardsize:
        addAttackList(Position(pos.x, pos.y))
        pos.x = pos.x + 1
    pos.x = startPos.x
    pos.y = startPos.y
    
    #positive y
    while pos.y < boardsize:
        addAttackList(Position(pos.x, pos.y))
        pos.y = pos.y + 1
    pos.x = startPos.x
    pos.y = startPos.y
    
    #negative x
    while pos.x >= 0:
        addAttackList(Position(pos.x, pos.y))
        pos.x = pos.x - 1
    pos.x = startPos.x
    pos.y = startPos.y
        
    #negative y
    while pos.y >= 0:
        addAttackList(Position(pos.x, pos.y))
        pos.y = pos.y - 1
    pos.x = startPos.x
    pos.y = startPos.y
    
    #diagonal -x +y left bottom
    while pos.x >= 0 and pos.y < boardsize:
        addAttackList(Position(pos.x, pos.y))
        pos.x = pos.x - 1
        pos.y = pos.y + 1
    pos.x = startPos.x
    pos.y = startPos.y
    
    #diagonal -x -y left top
    while pos.x >= 0 and pos.y >= 0:
        addAttackList(Position(pos.x, pos.y))
        pos.x = pos.x - 1
        pos.y = pos.y - 1
    pos.x = startPos.x
    pos.y = startPos.y
    
    #diagonal +x +y right bottom
    while pos.x < boardsize and pos.y < boardsize:
        addAttackList(Position(pos.x, pos.y))
        pos.x = pos.x + 1
        pos.y = pos.y + 1
    pos.x = startPos.x
    pos.y = startPos.y
    
    #diagonal +x -y right top
    while pos.x < boardsize and pos.y >= 0:
        addAttackList(Position(pos.x, pos.y))
        pos.x = pos.x + 1
        pos.y = pos.y - 1
    pos.x = startPos.x
    pos.y = startPos.y

    return attackList

def isInList(valid_positions, pos):
    assert isinstance(pos, Position)
    for position in valid_positions:
        if pos.compare(position):
            return pos
    return False

# This function goes through, places a queen in the first valid square, and removes all
# squares that are now invalid. This function takes a horizontal approach.
def placeXQueen(valid_positions, boardsize):    
    for i in range(0, boardsize):
        for j in range(0, boardsize):
            if isInList(valid_positions, Position(i,j)):
                invalidated_positions = generateQueenAttacks(boardsize, Position(i,j))
                for position in invalidated_positions:
                    pos = isInList(valid_positions, position):
                    if pos:
                        valid_positions.del(pos)
                return valid_positions

# This function goes through, places a queen in the first valid square, and removes all
# squares that are now invalid. This function takes a vertical approach.                
def placeYQueen(valid_positions, boardsize):    
    for i in range(0, boardsize):
        for j in range(0, boardsize):
            if isInList(valid_positions, Position(j,i)):
                invalidated_positions = generateQueenAttacks(boardsize, Position(j,i))
                for position in invalidated_positions:
                    pos = isInList(valid_positions, position):
                    if pos:
                        valid_positions.del(pos)
                return valid_positions

def solve(n):
    """ Takes a number n and generates solutions. """
    # Generate all initial positions

    # Generate initial starting position to place
    
    # Only call place X Queen
    # Only call place Y queen
    # Mark how many times either function returns successfully
    # 
    pass
        


if __name__ == "__main__":
    print "Basic board testing"
    #board = Board(1)
    #board.solve()
    #board = Board(4)
    #board.solve()
    board = makeBoard(4)
    for square in board:
        print square

    print "Basic position testing"
    pa = Position(1,1)
    pb = Position(2,2)
    pc = Position(1,1)
    pd = pa
    print "pa == pc: {}".format(pa == pc)
    print "pa == pb: {}".format(pa == pb)
    print "pa == pd: {}".format(pa == pd)
    pa.x += 1
    print pa
    
    print "Generating Queen attacks"
    for pos in generateQueenAttacks(4, Position(0,0)):
        print pos

    print "Recursivequeen call"
    recursiveQueen(makeBoard(4), 4, 4)
    
