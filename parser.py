import sys


def parser():
    with open('map.txt') as file:
        try:
            all_lines = file.readlines()
            req_lines = [line for line in all_lines if not line.startswith('#')]
            req_lines = [item for cell in list(map(str.split, req_lines)) for item in cell]
            req_lines = [x for x in filter(lambda x: x[0] != '#', req_lines)]
            for elem in req_lines:
                for sign in elem:
                    if not sign.isalpha():
                        print('Map error')
                        sys.exit()
            size = int(req_lines.pop(0))
            mapa = list(map(int, [item for cell in req_lines for item in cell]))
        except TypeError as e:
            print(e)
    if not len(mapa) % size == 0 and not len(mapa) / size == size:
        print('Size error')
        sys.exit()
    print(size)
    print(mapa)


parser()
