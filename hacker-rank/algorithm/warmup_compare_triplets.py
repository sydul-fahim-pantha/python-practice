#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    l = [0, 0, 0]
    
    for i in arr: 
        if i > 0: l[0] += 1
        elif i == 0: l[1] += 1     
        elif i < 0: l[2] += 1
    
    print('\n'.join(map(str, [l])))         

    arr = list(m
if __name__  == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
