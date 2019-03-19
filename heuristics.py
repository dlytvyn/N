import math


def manhattan_distance(size, board, target):
    distances = []
    for i in range(size * size):
        if not board[i] == target[i] and not board[i] == 0:
            distances.append(abs(target.index(board[i]) // size - i // size) +
                             abs(target.index(board[i]) % size - i % size))
    return sum(distances)


def euclidean_distance(size, board, target):
    distances = []
    for i in range(size * size):
        if not board[i] == target[i] and not board[i] == 0:
            # distances.append(math.pow((target.index(board[i]) // size - i // size) +
            #                           (target.index(board[i]) % size - i % size), 2))
            dy = abs(target.index(board[i]) // size - i // size)
            dx = abs(target.index(board[i]) % size - i % size)
            distances.append(dx * dx + dy * dy)
    return sum(distances)


def chebyshev_distance(size, board, target):
    distances = []
    for i in range(size * size):
        if not board[i] == target[i] and not board[i] == 0:
            distances.append(max((target.index(board[i]) // size - i // size),
                                 (target.index(board[i]) % size - i % size)))
    return sum(distances)


heuristics = {1: manhattan_distance,
              2: euclidean_distance,
              3: chebyshev_distance}
