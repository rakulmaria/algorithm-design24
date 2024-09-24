import sys

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
    # items is a list of tuples, with value and weight. (0,0)
    items = [(0, 0)]

    # the memory table, 2 x 2 array 
    memory = [[0 for i in range(C+1)] for j in range(n+1)]

    for i in range(1, n+1):
        value, weight = input().split()
        items.append((int(value), int(weight)))

    # solve the knapsack problem for this current knapsack
    solve(n, C)

    res = backtrack(len(memory)-1, len(memory[0])-1)
    lst = ""

    # how many items were taken
    print(len(res))

    for i in range(len(res)-1, -1, -1):
        print(res[i], end=" ")
        #lst += str(res[i]) + " "
    print(lst)
    
    # startover
    line = sys.stdin.readline()