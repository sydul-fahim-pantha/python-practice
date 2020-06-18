#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    
    start  = max(a)
    end = min(b)
    
    i_considered_count = 0

    i = start
    
    while i <= end: 
    
        i_considered = True
        
        for a_item in a: 
            if i % a_item != 0: 
                i_considered = False
                break
        if i_considered: 
            for b_item in b:
                if b_item % i != 0:
                    i_considered = False
                    break
        if i_considered: i_considered_count += 1  

        i += start

    print(i_considered_count)       

    return i_considered_count


if __name__ == '__main__':
    fptr = open('/home/sydul/Work/all_git_repos/personal_sydul_fahim_pantha/python-practice/hacker-rank/out.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
