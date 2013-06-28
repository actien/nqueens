# N queens
# Andy Tien
import copy, sys

class Position:
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
            return position
    return False

def placeQueen(valid_positions, pos, boardsize):
    if isInList(valid_positions, pos): #IS a valid position!
        invalid_positions = generateQueenAttacks(boardsize, pos)
        #update valid_positions
        for pos in invalid_positions:
            temp = isInList(valid_positions, pos)
            if temp:
                valid_positions.remove(temp)
        return True
    return False
            

def recursiveQueen(row, validList, queensLeft, boardsize, sol_stack):
    #print "============"
    #print "Currently on row {}".format(row)
    #print "Valid list is: {}".format(validList)
    #print "Queens left: {}".format(queensLeft)

    #assumption: in each version of the function, we will leave it making 
    #sure we have popped everything we pushed
    
    #clean up after myself.
    def cleanup(pushed):
        for i in range(0,pushed):
            sol_stack.pop()
    def print_solution():
        printingList = copy.deepcopy(sol_stack)
        printingList.reverse()
        print ", ".join(str(printingList[i]) for i in range(0, boardsize))
            

    if row > boardsize:
        return False
    elif len(validList) == 0:
        return False

    #make deep copy of validList to pass
    copiedList = copy.deepcopy(validList)
    pushed = 0
    for col in range(0, boardsize):
        #print col
        #sys.stdout.write("considering: {} ".format(Position(row, col)))
        if placeQueen(copiedList, Position(row, col), boardsize):
            sol_stack.append(Position(row,col))
            pushed += 1
            queensLeft = queensLeft - 1
            #sys.stdout.write("placed. {} queens left.\n".format(queensLeft))
            if queensLeft == 0: #solution!
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
        else:
            #sys.stdout.write("...failed.\n")
            pass
   
    # do we still have leftovers? clean them up
    cleanup(pushed)
    return False
        

    # row = which row we're in
    # the current position we are considering is: (row, col)

    # base cases: position checks out. is in valid list.
    # Compute new valid list for this version. Then:
    #   -> call recursiveQueen if queensLeft > 0 (recursive call). decrement queensLeft by 1, pass a new validList, and my row+1
    #   -> if queensLeft == 0, we just placed our last queen! We have a solution. add it to a solutions list.
    # If we reach end of col loop (meaning there are no valid positions in this row), return to our caller.
    #

def solve(n):
    originalboard = makeBoard(n)
    #print "Boardsize: {}".format(originalboard)
    recursiveQueen(0, originalboard, n, n, [])
    
    
    
if __name__ == "__main__":
##    print "Basic board testing"
##    #board = Board(1)
##    #board.solve()
##    #board = Board(4)
##    #board.solve()
##    board = makeBoard(4)
##    for square in board:
##        print square
##
##    print "Basic position testing"
##    pa = Position(1,1)
##    pb = Position(2,2)
##    pc = Position(1,1)
##    pd = pa
##    print "pa == pc: {}".format(pa == pc)
##    print "pa == pb: {}".format(pa == pb)
##    print "pa == pd: {}".format(pa == pd)
##    pa.x += 1
##    print pa
####    
##    print "Generating Queen attacks"
##    #for pos in generateQueenAttacks(4, Position(0,0)):
##     #   print pos
##    positions = makeBoard(4)
##    for pos in positions:
##        print pos
##    placeQueen(positions, Position(0,0), 4)
##    for pos in positions:
##        print pos
####
##    print "Recursivequeen call"
    solve(int(sys.argv[1]))
