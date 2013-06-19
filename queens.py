# N queens
# Andy Tien

class Position:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Board:
    def __init__(self, n):
        self.valid_positions = []
        # Make default positions
        for i in range(0, n):
            for j in range(0,n):
                self.valid_positions.append(Position(i,j))

        self.queens_left = n
        self.size = n


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
