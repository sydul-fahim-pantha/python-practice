#!/bin/python3

import os

# Complete the luckBalance function below.
def luckBalance(k, contests):
    imp_luck_i = []
    
    unimportant_luck = 0
    for row in contests:
        if row[1] == 1: imp_luck_i.append(row[0])
        elif row[1] == 0: unimportant_luck += row[0]
            
    imp_luck_i = reversed(sorted(imp_luck_i))
    # print('imp_luck_i', [i for i in imp_luck_i])

    important_luck = 0
    visited_imp_contest = {}

    for luck in imp_luck_i: 
        
        for i, row in enumerate(contests): 
            if i not in visited_imp_contest and row[0] == luck and row[1] == 1:
                visited_imp_contest[i] = True
                
                # check if I can lose
                if k > 0:
                    important_luck += luck
                    k -= 1
                else: 
                    important_luck -= luck    

    return important_luck + unimportant_luck


if __name__ == '__main__':
    fptr = open('/home/sydul/Work/all_git_repos/personal_sydul_fahim_pantha/python-practice/hacker-rank/f.txt', 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
