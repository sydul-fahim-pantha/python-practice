#!/bin/python3

import os


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    highest = ar[0]
    highest_count = 1
    
    for i in range(1, len(ar)):
        if highest < ar[i]: 
            highest = ar[i]
            highest_count = 1
        elif highest == ar[i]: 
            highest_count += 1
   
    return highest_count        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
