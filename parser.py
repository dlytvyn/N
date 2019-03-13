import sys


def parser():
    with open("map.txt") as file:
        all_lines = file.readlines()
    req_lines = [line for line in all_lines if not line.startswith('#')]
    mapa = [line.split('#')[0].strip() for line in req_lines]
    mapa = [item for line in mapa for item in line.split()]
    size = mapa.pop(0)
    for item in mapa:
        for sign in item:
            if not sign.isdigit():
                print('Map error!')
                sys.exit()
    mapa = list(map(int, mapa))
    print(size)
    print(mapa)


parser()