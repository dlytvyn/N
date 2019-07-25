from puzzle import Puzzle
from solver import Solver
from parser_file import Parser
from board import Board
from datetime import datetime


def main():
    start = datetime.now()
    parser = Parser()
    board = Board(parser.board)
    puzzle = Puzzle(parser.size, parser.heuristics, board)
    Solver(puzzle).a_star()
    end = datetime.now()
    print("Time = ", end - start)


if __name__ == '__main__':
    main()
