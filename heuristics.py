def manhattan_distance(size, board, target):
    sum = 0
    for i in range(size * size):
        if not board[i] == 0:
            b, t = i, target.index(board[i])
            sum += abs(b % size - t % size) + abs(b // size - t // size)
    # for i in range(size * size):
    #     if not board[i] == target[i] and not board[i] == 0:
    #         # sum += (abs(target.index(board[i]) // size - i // size) +
    #         #         abs(target.index(board[i]) % size - i % size))
    #         sum += abs(board[i]) + abs()
    return sum


def euclidean_distance(size, board, target):
    sum = 0
    for i in range(size * size):
        if not board[i] == target[i] and not board[i] == 0:
            dy = abs(target.index(board[i]) // size - i // size)
            dx = abs(target.index(board[i]) % size - i % size)
            sum += (dx * dx + dy * dy)
    return sum


def chebyshev_distance(size, board, target):
    sum = 0
    for i in range(size * size):
        if not board[i] == target[i] and not board[i] == 0:
            sum += (max(abs(target.index(board[i]) // size - i // size),
                        abs(target.index(board[i]) % size - i % size)))
    return sum


def outta_place_heuristic(size, board, target):
    res = 0
    for i in range(size * size):
        if not board[i] == target[i] and not board[i] == 0:
            res += 1
    return res


heuristics = {
    1: manhattan_distance,
    2: euclidean_distance,
    3: chebyshev_distance,
    4: outta_place_heuristic,
}
