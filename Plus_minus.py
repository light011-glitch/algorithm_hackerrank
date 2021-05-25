#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    a = [1 if i>0 else -1 if i<0 else 0 for i in arr]
    print("{:.6f}".format(a.count(1)/n))
    print("{:.6f}".format(a.count(-1)/n))
    print("{:.6f}".format(a.count(0)/n))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
