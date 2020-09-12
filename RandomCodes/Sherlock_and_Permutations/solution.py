def result(n0, n1):
    result = 1
    for i in range((n1 + 1), (n0 + n1 + 1)):
        result = (result * i) // (i - n1)
    print(result)
n = int(input())
for i in range(n):
    m,n = map(int,input().split())
    result(m,n-1)