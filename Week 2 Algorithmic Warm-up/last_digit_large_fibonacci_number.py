def digit_fib_num(n):
    if n <= 1:
        return n
    start = 0
    end = 1
    for i in range(n-1):
        start, end = end % 10, (start  + end) % 10
    return end % 10

num = int(input())
print(digit_fib_num(num))