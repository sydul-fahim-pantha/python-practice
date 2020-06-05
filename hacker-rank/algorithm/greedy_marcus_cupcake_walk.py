#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie.sort()
    calorie.reverse()
    
    miles = 0
    for index, i in enumerate(calorie): miles += pow(2, index) * i
    
    return miles
    # One line solution 
    # return sum( pow(2, index) * i for index, i in enumerate(sorted(calorie, reverse=True)))

if __name__ == '__main__':
    fptr = open('/home/sydul/Work/all_git_repos/personal_sydul_fahim_pantha/python-practice/hacker-rank/out.txt', 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
