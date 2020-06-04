#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
   
    last_diff = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        diff =  abs(arr[i] - arr[i+1])
        if diff < last_diff: last_diff = diff
    
    return last_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
