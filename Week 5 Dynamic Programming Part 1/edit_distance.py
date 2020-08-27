def edit_distance(st1, st2, a, b):
    D = [[0 for x in range(b+1)] for x in range(a+1)]
    for i in range(a+1):
        for j in range(b+1):
            if i == 0:
                D[i][j] = j
            elif j == 0:
                D[i][j] = i
            elif st1[i-1] == st2[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                D[i][j] = 1 + min(D[i][j-1], D[i-1][j], D[i-1][j-1])
    return D[a][b]

st1 = input()
st2 = input()
a = len(st1)
b = len(st2)
print(edit_distance(st1, st2, a, b))
