def overlap_times(n):
    group = []
    for i in range(n):
        a, b = map(int, input().split())
        group.append((a, b))
    group.sort(key = lambda x: x[1])
    index = 0
    coordinates = []
    while index < n:
        current = group[index]
        while index < n - 1 and current[1] >= group[index+1][0]:
            index += 1
        coordinates.append(current[1])
        index += 1
    ans = ""
    for i in coordinates:
        ans += (str(i) + " ")
    return str(len(coordinates)) + "\n" + ans

print(overlap_times(int(input())))