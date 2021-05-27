#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    lcm_arr = functools.reduce(lambda x,y:x*y//math.gcd(x,y),arr)
    gcd_brr = functools.reduce(math.gcd,brr)
    return sum([1 for x in range(lcm_arr,gcd_brr+1,lcm_arr) if gcd_brr%x == 0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
