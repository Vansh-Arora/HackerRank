def lights(n):
    print((pow(2,n) - 1) % 100000)

T = int(input())

for i in range(T):
    n = int(input())
    lights(n)