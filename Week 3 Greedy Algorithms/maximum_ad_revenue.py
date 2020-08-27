def max_revenue(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    sum = 0
    for i in range(n):
        sum += (a[i-1] * b[i-1])
    return sum

print(max_revenue(int(input())))