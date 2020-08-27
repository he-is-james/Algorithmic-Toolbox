import numpy

def knapsack(W, n, w):
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if w[j-1] <= i:
                t = value[i-w[j-1]][j-1] + w[j-1]
                if t > value[i][j]:
                    value[i][j] = t
    return int(value[W][n])

W, n = map(int, input().split())
w = list(map(int, input().split()))
print(knapsack(W, n, w))