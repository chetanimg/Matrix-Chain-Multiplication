import sys

mem = dict()


def initalizeMem(n):

    for i in range(1, n):
        for j in range(1, n):
            key = str(i) + "," + str(j)
            mem.update({key: sys.maxint})
    return mem


def MatrixChainOrder(p, i, j):

    if len(p) < 3:
        return 0

    key = str(i) + "," + str(j)
    if mem[key] < sys.maxint:
        return mem[key]
    if i == j:
        mem[key] = 0
    else:
        for k in range(i, j):
            q = MatrixChainOrder(p, i, k) + MatrixChainOrder(p, k + 1, j) + p[i-1] * p[k] * p[j]
            if q < mem[key]:
                mem[key] = q
    return mem[key]
