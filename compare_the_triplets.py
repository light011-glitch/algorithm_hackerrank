#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice = (1 if (a[0]>b[0]) else 0) + (1 if (a[1]>b[1]) else 0) + (1 if (a[2]>b[2]) else 0)
    bob = (1 if (a[0]<b[0]) else 0) + (1 if (a[1]<b[1]) else 0) + (1 if (a[2]<b[2]) else 0)
    return (alice,bob)  
    
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
