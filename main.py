from puzzle import Puzzle
from solver import Solver
from datetime import datetime
from parser_file import Parser


def main():
    start = datetime.now()
    parser = Parser()
    puzzle = Puzzle()
    solver = Solver(puzzle).a_star()
    end = datetime.now()
    print("Time = ", end - start)


if __name__ == '__main__':
    main()
