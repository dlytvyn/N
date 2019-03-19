from board import Board
from bisect import insort_left


class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.closed = set()
        self.open_list = [self.puzzle.parent]
        self.open_dict = {self.puzzle.parent.hash: self.puzzle.parent}
        self.target = str(puzzle.target)
        self.complexity_in_size = 0

    def a_star(self):
        while self.open_list:
            board = self.open_dict[self.open_list.pop(0).hash]
            if board.hash == self.target:
                return self.print_result(board, self.puzzle.size)
            del self.open_dict[board.hash]
            if board.hash not in self.closed:
                self.closed.add(board.hash)
                for move in self.puzzle.possible_moves[board.zero_coor]:
                    item = board.zero_coor + move
                    new_board = board.board[:]
                    new_board[board.zero_coor], new_board[item] = new_board[item], new_board[board.zero_coor]
                    new_hash = str(new_board)
                    if new_hash == self.puzzle.target:
                        return self.print_result(Board(new_board, board), self.puzzle.size)
                    if new_hash not in self.closed:
                        new_list_elem = Board(new_board, board)
                        self.puzzle.get_heuristic_coef(new_list_elem)
                        if (new_hash not in self.open_dict) or \
                            (new_hash in self.open_dict and
                             new_list_elem.g < self.open_dict[new_hash].g and
                             new_list_elem.h < self.open_dict[new_hash].h):
                            self.open_dict[new_hash] = new_list_elem
                            insort_left(self.open_list, new_list_elem)
                            self.complexity_in_size += 1

    def print_result(self, board, size):
        self.print_stack(board, size)
        print('\nComplexity in size = ', self.complexity_in_size)
        print('Complexity in time = ', self.closed.__len__())
        print('Total number of moves = ', board.g)
     #   print('Heuristic function: ', self.puzzle.heuristics)

    def print_stack(self, board, size):
        if board.parent:
            self.print_stack(board.parent, size)
        print('\n------- Step = ', board.g, ' -------')
        for i in range(size):
            print(board.board[i * size: size * (i + 1)])
