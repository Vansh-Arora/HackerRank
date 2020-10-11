# Problem Statement: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# find bribes

t = int(input())
i = 0
while i<t:
    i+=1
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    bribes = 0
    flag = 1
    for i in range(n-1):
        if a[i] > i+1:
            bribe = a[i] - (i+1)
            if bribe > 2:
                flag = 0
                print("Too chaotic")
                break
            bribes = bribes + bribe
    if(flag):
        print(bribes)
