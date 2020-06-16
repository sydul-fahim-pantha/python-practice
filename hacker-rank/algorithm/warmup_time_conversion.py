#!/bin/python3

import os
import sys

def timeConversion(s):
    am_pm = s[len(s) - 2: len(s)]
    hh = int(s[0:2])

    s = s[:len(s) - 2]
    print(s)

    if am_pm == 'AM' and hh == 12: s = '00' + s[2:]
    elif am_pm == 'PM' and hh != 12: s = str(12 + hh) + s[2:]
        
    print(s)

    return s    
   
if __name__ == '__main__':
    f = open('/home/sydul/Work/all_git_repos/personal_sydul_fahim_pantha/python-practice/hacker-rank/out.txt', 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
