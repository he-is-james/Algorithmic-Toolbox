def change(m):
    min_coins = [0] + ([float("inf")] * m)
    for i in range(m + 1):
        for c in coins:
            if i >= c:
                count = min_coins[i - c] + 1
                if count < min_coins[i]:
                    min_coins[i] = count
    return min_coins[m]

m = int(input())
coins = [1, 3, 4]
print(change(m))