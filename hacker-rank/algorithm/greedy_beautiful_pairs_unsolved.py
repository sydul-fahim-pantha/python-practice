#!/bin/python3

import os

# Complete the beautifulPairs function below.
def beautifulPairs(A, B):
    A.sort()
    B.sort()
    
    # prepare pairs
    beautiful_pairs = []
    for i, a in enumerate(A):
        for j, b in enumerate(B): 
            if (a == b):  beautiful_pairs.append([i, j])
            elif a < b: break

    print(beautiful_pairs)

    # find index to remove
    repeating_items_index = []
    for i in range(len(beautiful_pairs) - 1): 
        if beautiful_pairs [i][0] == beautiful_pairs[i + 1][0] or beautiful_pairs [i][1] == beautiful_pairs[i + 1][1]: 
            repeating_items_index.append(i)
    
    print('>>>>>>>>>>>>>>>>>.', set(A) - set(B))
    print(beautiful_pairs)
    print(repeating_items_index)
    print(len(beautiful_pairs) - len(repeating_items_index))
    print(len(beautiful_pairs) - len(repeating_items_index) + (1 if len(set(A) - set(B)) > 0 else 0))
    return len(beautiful_pairs) - len(repeating_items_index) + (1 if len(set(A) - set(B)) > 0 else 0)


if __name__ == '__main__':
    fptr = open('/home/sydul/Work/all_git_repos/personal_sydul_fahim_pantha/python-practice/hacker-rank/bla.txt', 'w')

    n = int(input())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
