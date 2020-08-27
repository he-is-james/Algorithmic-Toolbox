import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def strip(x_points, y_points, d, mn):
    ln_x = len(x_points)
    mid = x_points[ln_x//2][0]
    sub_y = [x for x in y_points if mid - d <= x[0] <= mid + d]
    ln_y = len(sub_y)
    minimum = d
    for j in range(ln_y - 1):
        for k in range(j + 1, min(j +5, ln_y)):
            a, b = sub_y[j], sub_y[k]
            dis = distance(a, b)
            if dis < minimum:
                mn = a, b
                minimum = dis
    return mn[0], mn[1], minimum

def quick(x_points):
    min_value = distance(x_points[0], x_points[1])
    p1 = x_points[0]
    p2 = x_points[1]
    if len(x_points) == 2:
        return p1, p2, min_value
    for i in range(len(x_points) - 1):
        for j in range(i +1, len(x_points)):
            if i != 0 and j != 1:
                d = distance(x_points[i], x_points[j])
                if d < min_value:
                    min_value = d
                    p1, p2 = x_points[i], x_points[j]
    return p1, p2, min_value

def close_point(x_points, y_points):
    ln_x_p = len(x_points)
    if ln_x_p <= 3:
        return quick(points)
    m = ln_x_p // 2
    Lx = x_points[:m]
    Rx = x_points[m:]
    midpoint = x_points[m][0]
    Ly = []
    Ry = []
    for i in y_points:
        if i[0] < midpoint:
            Ly.append(i)
        else:
            Ry.append(i)
    pl, ql, left = close_point(Lx, Ly)
    pr, qr, right = close_point(Rx, Ry)
    if left <= right:
        d = left
        mn = (pl, ql)
    else:
        d = right
        mn = (pr, qr)
    p, q, mid = strip(x_points, y_points, d, mn)
    if d <= mid:
        return mn[0], mn[1], d
    else:
        return p, q, mid

def final(points):
    x_points = sorted(points, key = lambda x: x[0])
    y_points = sorted(points, key = lambda x: (x[1], x[0]))
    p1, p2, result = close_point(x_points, y_points)
    return result

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
print(final(points))