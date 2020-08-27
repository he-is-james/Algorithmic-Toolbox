import numpy

def eq_partitions(W, n, v_list):
    if n < 3:
        return 0
    elif sum(v_list) % 3 != 0:
        return 0
    else:
        count = 0
        value = numpy.zeros((W+1, n+1))
        for i in range(1, W+1):
            for j in range(1, n+1):
                value[i][j] = value[i][j-1]
                if v_list[j-1] <= i:
                    t = value[i-v_list[j-1]][j-1] + v_list[j-1]
                    if t > value[i][j]:
                        value[i][j] = t
                if value[i][j] == W:
                    count += 1
    if count < 3:
        return 0
    else:
        return 1


n = int(input())
v_list = list(map(int, input().split()))
W = sum(v_list)//3
print(eq_partitions(W, n, v_list))