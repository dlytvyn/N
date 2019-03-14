def rotate(l, n):
    return l[-n:] + l[:-n]


def spiral_map(m, n, a):
    k, l = 0, 0

    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''
    a = rotate(a, -1)
    res = []
    while k < m and l < n:
        # Append the first row from the remaining rows
        for i in range(l, n):
            res.append(a[k][i])
        k += 1
        # Append the last column from the remaining columns
        for i in range(k, m):
            res.append(a[i][n - 1])
        n -= 1
        # Append the last row from the remaining rows
        if k < m:

            for i in range(n - 1, (l - 1), -1):
                res.append(a[m - 1][i])
            m -= 1
        # Append the first column from the remaining columns
        if l < n:
            for i in range(m - 1, k - 1, -1):
                res.append(a[i][l])
            l += 1
    return res

#
# a = [[1, 2, 3, 4, 5, 6],
#      [7, 8, 9, 10, 11, 12],
#      [13, 14, 15, 16, 17, 18]]
#
# R = 3
# C = 6
# res = spiral_print(R, C, a)
# print('Resulat = ', res)
