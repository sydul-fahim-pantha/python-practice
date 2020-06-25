#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    candies = [1 for _ in arr]

    iteration = 0
    while iteration < 2:
        for i in range(0, n - 1):
            if arr[i] > arr[i + 1] and candies[i] == candies[i + 1]: candies[i] += 1
            elif arr[i] > arr[i + 1] and candies[i] < candies[i + 1]: candies[i] = candies[i + 1] + 1
            elif arr[i] < arr[i + 1] and candies[i] == candies[i + 1]: candies[i + 1] += 1
            elif arr[i] < arr[i + 1] and candies[i] > candies[i + 1]: candies[i + 1] = candies[i] + 1

        iteration += 1   
        if (iteration == 1): 
            arr.reverse()
            candies.reverse()

    return sum(candies)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
