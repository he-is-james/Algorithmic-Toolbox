def gcd(x, y):
    if y == 0:
        return x
    d = x % y
    x = y
    y = d
    return gcd(x, y)

pair = list(map(int, input().split()))
a = max(pair)
b = min(pair)
print(gcd(a, b))