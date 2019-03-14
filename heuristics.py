
def manhattan_distance(size, board, target):
    distances = []
    for i in range(size * size):
        if not board[i] == target[i] and not board[i] == 0:
            distances.append(abs(target.index(board[i]) // size - board.index(board[i]) // size) + \
                             abs(target.index(board[i]) % size - board.index(board[i]) % size))
    return sum(distances)


heuristics = {1: manhattan_distance}
