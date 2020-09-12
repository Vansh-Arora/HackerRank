#!/bin/python3

import os
import sys
import math
# Complete the solve function below.
def solve(n, m):
    m = m - 1
    mplusn = m + n
    mfac = math.factorial(m)
    nfac = math.factorial(n)
    mplusnfac = math.factorial(mplusn)
    ans = int(mplusnfac / (mfac * nfac))
    return ans % (1000000007)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
