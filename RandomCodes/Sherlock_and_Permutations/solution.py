# The principle behind the code is based on the formula:
# n!/p!q! (where n is the total no. of positions to be filled, p and q are the number of teams a character repeats)
def result(n0, n1):
    result = 1
    for i in range((n1 + 1), (n0 + n1 + 1)):
        result = (result * i) // (i - n1)
    print(result % 1000000007)
n = int(input())
for i in range(n):
    m,n = map(int,input().split())
    result(m,n-1)