def digit_fib_num(n):
    if n <= 1:
        return n
    start = 0
    end = 1
    for i in range(n-1):
        start, end = end % 10, (start  + end) % 10
    return end

def fib_num(n):
    if n <= 1:
        return n
    start = 0
    end = 1
    for i in range(n-1):
        start, end = end, start  + end
    return end
    
def piasono_period(m):
    previous = 0
    current = 1
    for i in range(m * m + 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1

def fib_num_mod(n, m):
    remainder = n % piasono_period(m)
    return fib_num(remainder) % m

def partial_sum_of_fib_num(n, m):
    if n == m:
        return digit_fib_num(n)
    else:
        first = fib_num_mod(n + 1, 10) - 1
        last = fib_num_mod(m + 2, 10) - 1
    return (last - first) % 10

a, b = map(int, input().split())
print(partial_sum_of_fib_num(a, b))