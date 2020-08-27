def maj_element(seq, a, n):
    if a+1==n:
        return seq[a]
    elif a+2==n:
        return seq[a]
    mid = (a+n)//2
    left = maj_element(seq, a, mid)
    right = maj_element(seq, mid, n)

    cl, cr = 0, 0
    for i in seq[a:n]:
        if i == left:
            cl+=1
        elif i == right:
            cr+=1
    if cl>(n-a)//2 and left != -1:
        return left
    elif cr>(n-a)//2 and right != -1:
        return right
    else: 
        return -1
    
n = int(input())
seq = list(map(int, input().split()))
if maj_element(seq, 0, n) != -1:
    print(1)
else:
    print(0)