#!/bin/python3

import os

# Complete the gridChallenge function below.
def gridChallenge(grid):
    total_rows = len(grid)
    total_columns = len(grid[0])

    last_row = sorted(grid[0])
    
    for row in range(1, total_rows):
        current_row = sorted(grid[row])
        
        for column in range(total_columns): 
            if current_row[column] < last_row[column]: return 'NO'
        
        last_row = current_row
    
    return 'YES'        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
