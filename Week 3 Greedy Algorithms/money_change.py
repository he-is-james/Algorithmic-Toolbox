def change(num):
    coins = [10, 5, 1]
    count = 0
    while num > 0:
        for i in coins:
            count += num // i
            num %= i
    return count
num = int(input())
print(change(num))