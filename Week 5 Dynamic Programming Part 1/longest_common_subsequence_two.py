def subsequence(s1, s2, n1, n2):
    D = [[0 for x in range(n2+1)] for x in range(n1+1)]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            if s1[i-1] !=s2[j-1]:
                D[i][j] = max(D[i][j-1], D[i-1][j])
    return D[n1][n2]

n1 = int(input())
s1 = list(map(int, input().split()))
n2 = int(input())
s2 = list(map(int, input().split()))
print(subsequence(s1, s2, n1, n2))