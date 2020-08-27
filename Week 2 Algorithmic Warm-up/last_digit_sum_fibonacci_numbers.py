def digit_fib_num(n):
    if n <= 1:
        return n
    start = 0
    end = 1
    for i in range(n-1):
        start, end = end % 10, (start  + end) % 10
    return end

def get_sum_of_fib(n):
    new_num = (n + 2) % 60
    last_digit = digit_fib_num(new_num)
    if last_digit == 0:
        return 9
    else:
        return last_digit - 1

fib_num = int(input())
print(get_sum_of_fib(fib_num))