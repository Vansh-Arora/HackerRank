# solution is derived from AP sum formula S(n) = n/2(2a + (n-1)d)
def sum(n):
    print((n*n) % 1000000007)

T = int(input())
for i in range(T):
    n = int(input())
    sum(n)