import numpy as np

import sys

def print_memory(memory):
    for row in memory:
        print(f"{row}")

def solve(i, C):
    if i == 0:
        return 0
    if items[i][1] > C: # if the item weighs more than we have capacity of
        return solve(i-1, C)
    
    drop = solve(i-1, C)
    take = items[i][0] + solve(i-1, C-items[i][1]) # value of current item + optimal solution of previous item
    res = max(drop, take)

    memory[i][C] = res
    return res


def backtrack(row, col):
    res = []
    while row > 0 and col > 0:
        if memory[row][col] != memory[row-1][col]:
            res.append(row-1)
            col -= items[row][1]
        row -= 1

    return res



line = sys.stdin.readline()

while line:
    C, n = line.split()
    C = int(C)
    n = int(n)

    # items is a list of tuples, with value and weight
    items = np.empty((n + 1), tuple)

    # the memory table, 2 x 2 array 
    memory = np.zeros((n + 1, C + 1))

    for i in range(1, n+1):
        value, weight = input().split()
        items[i] = (int(value), int(weight))

    # solve the knapsack problem for this current knapsack
    solve(n, C)

    res = backtrack(len(memory)-1, len(memory[0])-1)
    lst = ""
    print(len(res))
    for i in range(len(res)-1, -1, -1):
        lst += str(res[i]) + " "
    print(lst)
    
    # startover
    line = sys.stdin.readline()