def bin_search(a, x):
    left, right = 0, len(a) -1
    while left <= right:
        mid = left + (right - left) // 2
        if x < a[mid]:
            right = mid - 1
        elif x > a[mid]:
            left = mid + 1
        else:
            return mid
    return -1

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = a[1:]
for x in b[1:]:
    print(bin_search(a, x), end = " ")