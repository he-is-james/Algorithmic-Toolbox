from math import inf

def calculate(n):
    operations = [0, 0] + [inf]*(n-1)
    for i in range(2, n+1):
        t1, t2, t3 = [inf]*3
        t1 = operations[i - 1] + 1
        if i % 2 == 0:
            t2 = operations[i // 2] + 1
        if i % 3 == 0:
            t3 = operations[i // 3] + 1
        operations[i] = min(t1, t2, t3)
    ans = ""
    m = n
    results = [n]
    while n != 1:
        if n % 3 == 0 and operations[n] - 1 == operations[n // 3]:
            results += [n // 3]
            n = n // 3
        elif n % 2 == 0 and operations[n] - 1 == operations[n // 2]:
            results += [n // 2]
            n = n // 2
        else:
            results += [n - 1]
            n -= 1
    results.reverse()
    for i in results:
        ans += str(i) + " "
    return str(operations[m]) + "\n" + ans

n = int(input())
print(calculate(n))