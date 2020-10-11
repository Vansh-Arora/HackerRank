# Problem Statement: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# find bribes

# Optimized O(n)

t = int(input())
j = 0
while j<t:
    j += 1
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    bribes = 0
    flag = 1
    for i in range(n):
        if (a[i] - (i+1))>2:
            bribes = "Too chaotic"
            flag = 0
            break

    if(flag):
        for i in range(n-1,-1,-1):
            if a[i] != i+1:
                if a[i-1] == i+1:
                    bribes += 1
                    a[i-1],a[i] = a[i],a[i-1]
                else:
                    bribes += 2
                    a[i-2] = a[i-1]
                    a[i-1] = a[i]
                    a[i] = i+1


    
    print(bribes)