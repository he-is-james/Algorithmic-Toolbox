def contain_point(group):
    points = list(map(int, input().split()))
    for i in points:
        group.append((i, "p"))

    group.sort()
    point_in_seg = dict()
    count = 0
    for t in group:
        if t[1] == "l":
            count += 1
        elif t[1] == "r":
            count -= 1
        else:
            point_in_seg[t[0]] = count
            print(point_in_seg)
    result = ""
    for j in points:
        result += str(point_in_seg[j]) + " "
    return result[:-1]

s, p = map(int, input().split())
group = []
for i in range(s):
    c, d = map(int, input().split())
    group.append((c, "l"))
    group.append((d, "r"))
print(contain_point(group))
