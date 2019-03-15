import sys


def parser():
    try:
        with open("maps/test4x4") as file:
            all_lines = file.readlines()
        req_lines = [line for line in all_lines if not line.startswith('#')]
        mapa = [line.split('#')[0].strip() for line in req_lines]
        mapa = [item for line in mapa for item in line.split()]
        size = int(mapa.pop(0))
        for item in mapa:
            for sign in item:
                if not sign.isdigit():
                    print('Map error!')
                    sys.exit()
        mapa = list(map(int, mapa))
        return mapa, size
    except Exception as e:
        print(e)
        sys.exit(0)
