import sys
from argparse import ArgumentParser, FileType, RawTextHelpFormatter, ArgumentTypeError
from random import choice

from heuristics import heuristics


class Parser:
    def __init__(self):
        self.arguments = self.get_arguments()
        self.board = None
        self.size = None
        self.heuristics = heuristics[self.arguments.heuristic_number]
        if self.arguments.random_size:
            self.generate_random_map()
        elif self.arguments.file:
            self.parse_file(self.arguments.file.name)
        if not self.is_solvable():
            print('This puzzle is not solvable!')
            sys.exit(0)

    def parse_file(self, file_name):
        try:
            with open(file_name) as file:
                all_lines = file.readlines()
            req_lines = [line for line in all_lines if not line.startswith('#')]
            mapa = [line.split('#')[0].strip() for line in req_lines]
            mapa = [item for line in mapa for item in line.split()]
            self.validate_size(mapa[0])
            self.size = int(mapa.pop(0))
            for item in mapa:
                for sign in item:
                    if not sign.isdigit():
                        print('Map error!')
                        sys.exit()
            self.board = list(map(int, mapa))
            if len(self.board) != self.size ** 2:
                print("Puzzle size doesn't correspond!")
                sys.exit()
        except Exception as e:
            print(e)
            sys.exit(0)

    def show_usage(self):
        return('''
        main.py
        arguments:
            -f File
            -r Number (Number is the size of the map)
        heuristics:
            -h [1, 2, 3] (default is 1), where
                1: Manhattan distance
                2: Euclidean distance (squared)
                3: Chebyshev distance
        ''')

    def generate_random_map(self):
        self.size = int(self.arguments.random_size)
        elements = list(range(self.size ** 2))
        board = []
        while elements:
            a = choice(elements)
            board.append(a)
            elements.remove(a)
        self.board = board
        if not self.is_solvable():
            self.generate_random_map()

    def validate_size(self, strsize):
        size = int(strsize)
        if size < 3:
            raise ArgumentTypeError("Size is %s, but must be >= 3" % strsize)
        return size

    def get_arguments(self):
        parser = ArgumentParser(add_help=False, usage=self.show_usage(),
                                formatter_class=RawTextHelpFormatter)
        parser.add_argument('-f', type=FileType(), dest='file')
        parser.add_argument('-h', type=int,
                            choices=[1, 2, 3], action="store",
                            dest="heuristic_number", default=1)
        parser.add_argument('-r', type=self.validate_size,
                            dest="random_size", required=False)
        return parser.parse_args()

    def get_inv_count(self, board):
        invCount = 0
        for i in range(self.size * self.size - 1):
            for j in range(i + 1, self.size * self.size):
                if board[j] and board[i] and board[i] > board[j]:
                    invCount += 1
        return invCount

    def is_solvable(self):
        invCount = self.get_inv_count(self.board)
        if self.size % 2 == 1:
            return invCount % 2 == 1
        else:
            pos = self.size - (self.board.index(0) // self.size)
            if pos % 2 == 1:
                return not invCount % 2
            else:
                return invCount % 2
