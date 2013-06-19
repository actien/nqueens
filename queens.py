# N queens
# Andy Tien

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
        # Make default positions
        for i in range(0, n):
            for j in range(0,n):
                self.valid_positions.append(Position(i,j))

        self.queens_left = n
        self.size = n
    def _placeQueen(valid_positions, queen_position, boardsize):
        #Given the list of valid positions, the position we want to place the queen, 
        #and the boardsize, return a new list of positions that would be invalidated
        pass
        
    def solve(self):
        print "Solving n-queens problem"


if __name__ == "__main__":
    board = Board(1)
    for pos in board.valid_positions:
        print pos
    print ""
    board = Board(2)
    for pos in board.valid_positions:
        print pos
    print ""
    board = Board(3)
    for pos in board.valid_positions:
        print pos
    print ""
    board = Board(4)
    for pos in board.valid_positions:
        print pos
