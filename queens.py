# N queens
# Andy Tien
import copy, sys

class Position:
    """ Position class to represent a position on the board.
        TODO: There might be a better way to do the 'compare' function, look into 
              python libs
    """
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def compare(self, other_position):
        assert isinstance(other_position, Position)
        return self.x == other_position.x and self.y == other_position.y

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
        Alternatively it may be good to use the elegant diagonal summation/difference
        checks.
    """
    assert isinstance(pos, Position) and validatePosition(boardsize, pos)
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
    """ Tests whether pos is in valid_positions using the compare function
        in the Position class. This allows us to set two different objects 
        equal. If it is, return the position pointer. Otherwise, return False.
    """
    assert isinstance(pos, Position)
    for position in valid_positions:
        if pos.compare(position):
            return position
    return False

def placeQueen(valid_positions, pos, boardsize):
    """ Tries to place a queen in the position that is passed. Calls isInList
        to help it decide. Returns True if the queen was successfully place, False
        otherwise.
    """
    if isInList(valid_positions, pos): #IS a valid position!
        invalid_positions = generateQueenAttacks(boardsize, pos)
        #update valid_positions
        for pos in invalid_positions:
            temp = isInList(valid_positions, pos)
            if temp:
                valid_positions.remove(temp)
        return True
    return False

def fancyprint(solutions_list, boardsize):
    for i in range(0, boardsize):
        for j in range(0, boardsize):
            if isInList(solutions_list, Position(i,j)):
                sys.stdout.write("Q")
            else:
                sys.stdout.write("#")
        sys.stdout.write("\n")


def recursiveQueen(row, validList, queensLeft, boardsize, sol_stack):
    """ Solve the N-queens problem recursively. Saves board state via deep copying
        the list of valid positions. Also maintains a solution stack that is passed
        to recursed instances of this function; the solution stack is used to keep
        track of the positions being considered as a solution to the n-queens problem.
    """
    #Internal helper functions
    def cleanup(pushed):
        for i in range(0,pushed):
            sol_stack.pop()
    def print_solution():
        printingList = sol_stack[-1*boardsize:] #slice for last 5 solutions
        print ", ".join(str(printingList[i]) for i in range(0, boardsize))
        fancyprint(printingList, boardsize)

    #Are we even on the board? Do we even have squares left to test?
    if row > boardsize:
        return False
    elif len(validList) == 0:
        return False

    #Save board state 
    copiedList = copy.deepcopy(validList)
    pushed = 0
    for col in range(0, boardsize):
        if placeQueen(copiedList, Position(row, col), boardsize):
            sol_stack.append(Position(row,col))
            pushed += 1
            queensLeft = queensLeft - 1
            if queensLeft == 0: 
                print "Solution:"
                print_solution()
                cleanup(pushed)
                return True
            else: #keep going
                failed = recursiveQueen(row+1, copiedList, queensLeft, boardsize, sol_stack)
                if not failed: #reset list to last case, try next row
                    copiedList = copy.deepcopy(validList)
                    queensLeft += 1
                    pushed -= 1
                    sol_stack.pop()
    # do we still have leftovers? clean them up
    cleanup(pushed)
    return False
        
def solve(n):
    """ 'Main' function, makes the board, and then calls recursiveQueen.
    """
    originalboard = makeBoard(n)
    recursiveQueen(0, originalboard, n, n, [])
    
def basic_tests():
    print "Make Board testing"
    positions = makeBoard(4)
    for pos in positions:
        print pos

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
    
    print "generating Queen attacks test"
    for pos in generateQueenAttacks(4, Position(0,0)):
        print pos

    print "placeQueen test"
    placeQueen(positions, Position(0,0), 4)
    for pos in positions:
        print pos
    
    
if __name__ == "__main__":
    solve(int(sys.argv[1]))
# tests: uncomment to run
#    basic_tests()
