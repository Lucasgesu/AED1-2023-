def Mergesort (a, p, r):
    if p < r:
        q = (p + r)/2
        Mergesort(a, p, q)
        Mergesort(a, q+1, r)
        inetercala (a, p, q, r)
def inetercala (a, p, q, r):
    i = p
    for i in range(p,q):
        B[0] = A[1]
    for j in range(q+1, r):
        B[r+q+1]