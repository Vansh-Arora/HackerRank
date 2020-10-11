# Problem Statement: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# find bribes

# Optimized O(n)
# Max No. of times a person can bribe is 2

t = int(input())
j = 0
while j<t:
    j += 1
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    bribes = 0
    flag = 1

    for i in range(n):
        if (a[i] - (i+1))>2:                     # To check if person has bribed more than 2 people.
            bribes = "Too chaotic"
            flag = 0
            break

    if(flag):
        for i in range(n-1,-1,-1):
            if a[i] != i+1:                       # Condition1: check if a person has bribed
                if a[i-1] == i+1:                 # Condition2: check if the no. has bribed the person on his left
                    bribes += 1
                    a[i-1],a[i] = a[i],a[i-1]     #               if yes: swap persons
                else:
                    bribes += 2                   #               else: The person must have swiped 2 persons
                    a[i-2] = a[i-1]               #               So, shift person at left toward one position left further
                    a[i-1] = a[i]                 #                   shift current person to one position left
                    a[i] = i+1                    #                    at current position put a[i] = i.

    print(bribes)