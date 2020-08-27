def gcd(x, y):
    if y == 0:
        return x
    d = x % y
    x = y
    y = d
    return gcd(x, y)

def lcm(c, d):
    product = c * d
    multiple = int(product / gcd(c, d))
    return multiple

pair = list(map(int, input().split()))
a = max(pair)
b = min(pair)
print(lcm(a, b))