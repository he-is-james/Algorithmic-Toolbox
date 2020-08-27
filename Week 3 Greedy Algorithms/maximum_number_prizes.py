def prize_num(n):
    if n <= 2:
        return str(1) + "\n" + str(n)
    W = n
    prizes = []
    for i in range(1, n):
        if W > 2 * i:
            prizes.append(i)
            W -= i
        else:
            prizes.append(W)
            break
    ans = ""
    for l in prizes:
        ans += (str(l) + " ")
    return str(len(prizes)) + "\n" + ans

print(prize_num(int(input())))