import math

def distance(p1, p2):
    result = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return result

def quick_dis(n, points):
    if len(points) == 2:
        return distance(points[0], points[1])
    min_value = float("inf")
    for i in range(n-1):
        for j in range(i+1, n):
            if distance(points[i], points[j]) < min_value:
                min_value = distance(points[i], points[j])
    return min_value

def overlap(over, length, d):
    min_value = d
    over.sort(key=lambda x: x[1])
    for a in range(length):
        b = a + 1
        while b < length and (over[b][1] - over[a][1]) < min_value:
            min_value = distance(over[a], over[b])
            b += 1
    return min_value

def close_point(n, points):
    if n <= 3:
        return quick_dis(n, points)
    m = n//2
    left = close_point(m, points[:m])
    right = close_point(n-m, points[m:])
    d = min(left, right)
    over = []
    for i in range(n):
        if abs(points[i][0] - points[m][0]) < d:
            over.append(points[i])
    return min(d, overlap(over, len(over), d))
    
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort(key=lambda x: x[0])
print(close_point(n, points))