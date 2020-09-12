def sum(n):
    a = 1
    d = 2
    print( (n/2) * ( 2*a + (n-1)*d ) )

T = int(input())
for i in range(T):
    n = int(input())
    sum(n)