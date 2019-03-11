
class Board:
    h = 0

    def __init__(self, board, size):
        self.board = board
        self.zero_coor = self.board.index(0)
        self.size = size

    def calculate_h(self):
        for index, item in enumerate(self.board):
            if item != index + 1 and item != 0:
                self.h += 1
            if item == 0:
                self.zero_coor = index

    def make_copy(self):
        return self.board.copy()

    def swap(self, board, new_coor):
        if (new_coor % self.size != 0 and abs(new_coor - self.zero_coor) == 1) and (new_coor % self.size != 3):
            tmp = board[new_coor]
            board[new_coor] = board[self.zero_coor]
            board[self.zero_coor] = tmp
            return board
        else:
            return None

    def neighbors(self):
        boards_list = list()
        boards_list.append(self.swap(self.make_copy(), self.zero_coor - 1))
        boards_list.append(self.swap(self.make_copy(), self.zero_coor + 1))
        boards_list.append(self.swap(self.make_copy(), self.zero_coor - self.size))
        boards_list.append(self.swap(self.make_copy(), self.zero_coor + self.size))

