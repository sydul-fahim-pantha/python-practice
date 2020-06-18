#!/bin/python3

import os
import sys

def gcd(arr):
    divisors = []
    
    # find all the divisors for the first number 
    i = 1
    current_number= arr[0]
    while i <= arr[0] // 2:
        if current_number % i == 0:
            current_number = current_number / i
            divisors.append(i)
            i = 1
        else:
            i += 1
    divisors.append(current_number)            
    
    for i in range(1, len(arr)):
        divisors_index = 0
        while True:
            divisor = divisors[divisors_index]
            if arr[i] % divisor != 0:
                divisors.pop(divisor)
            else:
                divisors_index += 1    

         

   
if __name__ == '__main__':
    f = open('/home/sydul/Work/all_git_repos/personal_sydul_fahim_pantha/python-practice/hacker-rank/out.txt', 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
