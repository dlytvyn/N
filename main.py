from map_parser import parser
from puzzle import Puzzle
from solver import Solver
from datetime import datetime


def main():
    start = datetime.now()
    board, size = parser()
    puzzle = Puzzle(size, board)
    solver = Solver(puzzle).a_star()
    end = datetime.now()
    print("Time = ", end - start)


if __name__ == '__main__':
    main()
