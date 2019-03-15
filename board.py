
class Board:
    def __init__(self, board, parent=None):
        self.board = board
        self.zero_coor = self.board.index(0)
        self.parent = parent
        self.hash = str(self.board)
        self.g = parent.g + 1 if parent else 0
        self.h = 0
        self.f = 0

    def __lt__(self, new):
        if self.f == new.f:
            if self.h == new.h:
                return self.g < new.g
            return self.h < new.h
        return self.f < new.f
