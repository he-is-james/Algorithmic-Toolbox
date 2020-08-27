import math


def calculate(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    else:
        return x * y


def min_max(M, m, i, j, oper):
    min_v = math.inf
    max_v = -math.inf
    for k in range(i, j):
        a = calculate(M[i][k], M[k+1][j], oper[k])
        b = calculate(M[i][k], m[k+1][j], oper[k])
        c = calculate(m[i][k], M[k+1][j], oper[k])
        d = calculate(m[i][k], m[k+1][j], oper[k])
        min_v = min(min_v, a, b, c, d)
        max_v = max(max_v, a, b, c, d)
    return min_v, max_v


def parentheses(oper, nums):
    n = len(nums)
    m = [[0 for x in range(n)] for x in range(n)]
    M = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        m[i][i] = nums[i]
        M[i][i] = nums[i]
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j], M[i][j] = min_max(M, m, i, j, oper)
    return M[0][n-1]
    

exp = input()
oper, nums = [], []
for i in exp:
    if i in ["+", "-", "*"]:
        oper.append(i)
    else:
        nums.append(int(i))
print(parentheses(oper, nums))