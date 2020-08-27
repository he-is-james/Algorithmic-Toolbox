import random

def sort_3(seq, l, r):
    pivot = seq[l]
    p1 = i = l
    p2 = r
    while i <= p2:
        if seq[i] < pivot:
            seq[i], seq[p1] = seq[p1], seq[i]
            p1 += 1
            i += 1
        elif seq[i] == pivot:
            i += 1
        else:
            seq[i], seq[p2] = seq[p2], seq[i]
            p2 -= 1
        pIndex = [p1, p2]
    return pIndex

def random_quick_sort(seq, l, r):
    if l >= r:
        return
        
    pivot = random.randint(l, r)
    seq[l], seq[pivot] = seq[pivot], seq[l]
    pIndex = sort_3(seq, l, r)
    random_quick_sort(seq, l, pIndex[0] - 1)
    random_quick_sort(seq, pIndex[1] + 1, r)

r = int(input())
seq = list(map(int, input().split()))
random_quick_sort(seq, 0, r-1)
for x in seq:
    print(x, end = " ")