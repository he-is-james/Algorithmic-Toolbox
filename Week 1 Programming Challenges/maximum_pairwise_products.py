def max_pairwise_product(numbers):
    n = len(numbers)
    order = sorted(numbers)
    return order[n-2] * order[n-1]

input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))