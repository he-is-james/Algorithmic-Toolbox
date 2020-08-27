def digit_fib_num(n):
    if n <= 1:
        return n
    start = 0
    end = 1
    for i in range(n-1):
        start, end = end % 10, (start  + end) % 10
    return end

def sum_squares_fib(n):
    first = n % 60
    end = (n + 1) % 60
    if first <= 1:
        a = first
    else:
        a = digit_fib_num(first)
    if end <= 1:
        b = end
    else:
        b = digit_fib_num(end)
    return (a * b) % 10

fib_num = int(input())
print(sum_squares_fib(fib_num))