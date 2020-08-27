
import numpy as np

def knapsack(n, W):
    items = []
    for i in range(n):
        v, w = map(int, input().split())
        items.append((v, w))
    items.sort(key = lambda x: x[0]/x[1], reverse = True)
    value = 0
    for v, w in items:
        if W == 0:
            return value
        amount = min(w, W)
        value += amount * v / w
        W -= amount
    return round(value, 4)

n, W = map(int, input().split())
print(knapsack(n, W))