# Problem Statement: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# find bribes
# Brute Force Method (O(n^2))
t = int(input())
j = 0
while j<t:
    j+=1
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    bribes = 0
    for i in range(n):
        if (a[i] - (i+1))>2:
            bribes = "Too chaotic"
            break
        key = a[i]
        for k in range(i+1,n):
            if a[k] < key:
                bribes += 1
    print(bribes)
