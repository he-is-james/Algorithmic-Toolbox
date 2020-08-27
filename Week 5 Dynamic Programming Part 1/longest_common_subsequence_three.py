import numpy
def subsequence(s1, s2, s3, n1, n2, n3):
    D = numpy.zeros((n1+1, n2+1, n3+1))
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            for k in range(1, n3+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(D[i][j-1][k], D[i-1][j][k], D[i][j][k-1])
    return int(D[n1][n2][n3])

n1 = int(input())
s1 = list(map(int, input().split()))
n2 = int(input())
s2 = list(map(int, input().split()))
n3 = int(input())
s3 = list(map(int, input().split()))
print(subsequence(s1, s2, s3, n1, n2, n3))