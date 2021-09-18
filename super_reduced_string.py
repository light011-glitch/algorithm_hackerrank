   #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    if len(s) == 1:
        return(s)
    
    d = 1
    while d < len(s):
        if s[d] == s[d-1]:
            if len(s) == 2:
                return 'Empty String'
            s = s[:d-1] + s[d+1:]
            d = 1
        else:
            d += 1
            
    if len(s) == 0:
        return 'Empty String'
    else:
        return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
