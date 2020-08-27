def merge(B, C):
    D = []
    i, j, inver_counter = 0, 0, 0
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            inver_counter += len(B) - i
            j += 1
    D += B[i:]
    D += C[j:]
    return D, inver_counter

def merge_sort(A):
    global result
    if len(A) <= 1:
        return A
    m = len(A)//2
    L = merge_sort(A[:m])
    R = merge_sort(A[m:])
    sort_A, tee = merge(L, R)
    result += tee
    return sort_A

result = 0
n = int(input())
A = list(map(int, input().split()))
merge_sort(A)
print(result)