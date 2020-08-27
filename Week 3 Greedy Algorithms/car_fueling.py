def refuel(d):
    m = int(input())
    n = int(input())
    stops = [0]
    add = list(map(int, input().split()))
    stops += add
    stops.append(d)
    num_refuel, curr_refuel = 0, 0
    while curr_refuel <= n:
        last_refuel = curr_refuel
        while curr_refuel <= n and stops[curr_refuel + 1] - stops[last_refuel] <= m:
            curr_refuel += 1
        if curr_refuel == last_refuel:
            return -1
        elif curr_refuel <= n:
            num_refuel += 1
    return num_refuel
print(refuel(int(input())))
