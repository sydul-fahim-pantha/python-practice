#!/bin/python3

import os

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    A.sort()
    B.sort()

    l = []
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if (a == b): l.append([i, j])
    
    for i in range(len(l) - 1):
        if l[i][0] != -1: 
            for j in range(i + 1, len(l)):
                if l[i][0] == l[j][0] or l[i][1] == l[j][1]: 
                    l[j][0] = -1
                    l[j][1] = -1
     
    total_pair_count = len(l)
    
    for i in range(len(l)): 
        if l[i][0] == -1: total_pair_count -= 1

    if len(set(A) - set(B)) > 0: total_pair_count += 1
    elif len(A) == total_pair_count: total_pair_count -= 1

    diff = len(set(A) - set(B))
    print(len(A) - diff +1 if diff else len(A) - 1)
        
    return len(A) - diff +1 if diff else len(A) - 1


if __name__ == '__main__':
    fptr = open('/home/sydul/Work/all_git_repos/personal_sydul_fahim_pantha/python-practice/hacker-rank/bla.txt', 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
