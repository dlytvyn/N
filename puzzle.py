from heuristics import heuristics
from board import Board
from parser_file import Parser


class Puzzle(Parser):
    def __init__(self):
        super().__init__()
        self.length = self.size * self.size
        self.parent = Board(self.board)
        self.usual_puzzle = self.board.copy()
        self.usual_puzzle.sort()
        self.usual_puzzle.append(self.usual_puzzle.pop(0))
        self.target = [0 for i in range(self.length)]
        self.target_puzzle()
        self.target_dict = {item: i for i, item in enumerate(self.target)}
        self.possible_moves = self.search_moves()

    def target_puzzle(self):
        i, j = 0, 0
        move_i, move_j = 0, 1
        for n in range(0, self.length):
            self.target[i * self.size + j] = self.usual_puzzle[n]
            new_i = i + move_i
            new_j = j + move_j
            if 0 <= new_i < self.size and 0 <= new_j < self.size and self.target[new_i * self.size + new_j] == 0:
                i = new_i
                j = new_j
            else:
                move_j, move_i = -move_i, move_j
                i = i + move_i
                j = j + move_j

    def search_moves(self):
        possible_moves = {}
        for i in range(self.length):
            possible_moves[i] = []
            if (i % self.size) + 1 < self.size:
                possible_moves[i].append(1)
            if (i % self.size) - 1 >= 0:
                possible_moves[i].append(-1)
            if i + self.size < self.length:
                possible_moves[i].append(self.size)
            if i - self.size >= 0:
                possible_moves[i].append(-self.size)
        return possible_moves

    def get_h(self, board, target_puzzle):
        return heuristics[self.heuristics](self.size, board, target_puzzle)

    def get_heuristic_coef(self, board):
        board.h = self.get_h(board.board, self.target)
        board.f = board.g + board.h
