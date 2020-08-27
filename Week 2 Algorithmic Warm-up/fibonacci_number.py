def fib_num(n):
    if n <= 1:
        return n
    start = 0
    end = 1
    for i in range(n-1):
        start, end = end, start  + end
    return end
num = int(input())
print(fib_num(num))