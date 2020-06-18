#!/bin/python3

import os
import sys

def gcd(a,b):
    if a % b == 0: return b
    return gcd(b, a % b)    


def main():
    l = list(map(int, input().strip().split()))
    a = l[0]
    
    for i in range(1, len(l)): 
        a = gcd(a, l[i]) 
        print('gcd: ', a)
    
if __name__ == '__main__':
    main()
    