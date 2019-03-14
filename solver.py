from puzzle import Puzzle
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

    # def a_star(self):
    #     while self.open_list:
    #         board = self.open_dict[self.open_list.pop(0).hash]
    #         if board.hash == self.target:
    #             return self.print_result(board, self.puzzle.size)
    #         del self.open_dict[board.hash]
    #         if board.hash not in self.closed:
    #             self.closed.add(board.hash)
    #             for move in self.puzzle.possible_moves[board.zero_coor]:
    #                 item = board.zero_coor + move
    #                 new_board = board.board[:]
    #                 new_board[board.zero_coor], new_board[item] = new_board[item], new_board[board.zero_coor]
    #                 new_hash = str(new_board)
    #                 if new_hash == self.puzzle.target:
    #                     return self.print_result(Board(new_board, board), self.puzzle.size)
    #                 if new_hash not in self.closed:
    #                     new_board = Board(new_board, board)
    #                     self.puzzle.get_heuristic_coef(new_board)
    #                     if (new_hash not in self.open_dict) or \
    #                         (new_hash in self.open_dict and
    #                          new_board.g < self.open_dict[new_hash].g and
    #                          new_board.h < self.open_dict[new_hash].h):
    #                         self.open_dict[new_hash] = new_board
    #                         self.open_list.append(new_board)
    #                         self.complexity_in_size += 1


    def a_star(self):
        while self.open_list:
            board = self.open_dict[self.open_list[0].hash]
            if board.hash == self.target:
                return self.print_result(board, self.puzzle.size)
            # del self.open_dict[board.hash]
            if board.hash not in self.closed:

                self.closed.add(board.hash)   # delete from open list and add to closed list
                del self.open_dict[board.hash]
                del self.open_list[self.open_list.index(board)]

                for move in self.puzzle.possible_moves[board.zero_coor]:
                    item = board.zero_coor + move
                    new_board = board.board[:]
                    new_board[board.zero_coor], new_board[item] = new_board[item], new_board[board.zero_coor]
                    new_hash = str(new_board)
                    if new_hash == self.puzzle.target:
                        return self.print_result(Board(new_board, board), self.puzzle.size)
                    if new_hash not in self.closed:
                        new_board = Board(new_board, board)
                        self.puzzle.get_heuristic_coef(new_board)
                        if (new_hash not in self.open_dict) or \
                            (new_hash in self.open_dict and
                             new_board.g < self.open_dict[new_hash].g and
                             new_board.h < self.open_dict[new_hash].h):
                            self.open_dict[new_hash] = new_board
                            if self.open_list:
                                self.open_list.insert(0 if new_board.f < self.open_list[0].f else 1, new_board)
                            else:
                                self.open_list.append(new_board)
                            self.complexity_in_size += 1






    def print_result(self, board, size):
        for i in range(size):
            print(board.board[i * size: size * (i + 1)])
