import math
def dh3(a,b,r):
    if r<b or r<a:
        if r % math.gcd(a,b) == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
T = int(input())
assert(1<=T<=100)

for i in range(T):
    a,b,r = map(int,input().split())
    dh3(a,b,r)