# python3

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

num = input()
a, b = map(int, num.split())
print(sum_of_two_digits(a, b))