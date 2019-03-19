def spiral_map(m, n, a):
    k, l = 0, 0

    a = a[-1:] + 1[:-1]
    res = []
    while k < m and l < n:
        for i in range(l, n):
            res.append(a[k][i])
        k += 1
        for i in range(k, m):
            res.append(a[i][n - 1])
        n -= 1
        if k < m:

            for i in range(n - 1, (l - 1), -1):
                res.append(a[m - 1][i])
            m -= 1
        if l < n:
            for i in range(m - 1, k - 1, -1):
                res.append(a[i][l])
            l += 1
    return res
