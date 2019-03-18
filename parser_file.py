import sys
from argparse import ArgumentParser, FileType, RawTextHelpFormatter


class Parser:
    def __init__(self):
        self.arguments = self.get_arguments()
        self.board = None
        self.size = None
        self.heuristics = int(self.arguments.heuristic_number)
        if self.arguments.file:
            self.parse_file(self.arguments.file.name)

    def parse_file(self, file_name):
        try:
            with open(file_name) as file:
                all_lines = file.readlines()
            req_lines = [line for line in all_lines if not line.startswith('#')]
            mapa = [line.split('#')[0].strip() for line in req_lines]
            mapa = [item for line in mapa for item in line.split()]
            self.size = int(mapa.pop(0))
            for item in mapa:
                for sign in item:
                    if not sign.isdigit():
                        print('Map error!')
                        sys.exit()
            self.board = list(map(int, mapa))
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
                2: Euclidean distance
                3: Chebyshev distance
        ''')

    def generate_random_map(self):
        pass

    def get_arguments(self):
        parser = ArgumentParser(add_help=False, usage=self.show_usage(),
                                formatter_class=RawTextHelpFormatter)
        parser.add_argument('-f', type=FileType(), dest='file')
        parser.add_argument('-h', type=int,
                            choices=[1, 2, 3], action="store",
                            dest="heuristic_number", default=1)
        parser.add_argument('-r', '--random', type=self.generate_random_map,
                            dest="random_size", required=False)
        return parser.parse_args()
