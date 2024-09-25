import sys

def solve(C, n, items, memory):
    for i in range(1, n):
        value = items[i][0]
        weight = items[i][1]

        for cur_cap in range(1, C):
            # assume we don't take the current item
            memory[i][cur_cap] = memory[i-1][cur_cap]
            take = memory[i-1][cur_cap-weight] + value
            drop = memory[i][cur_cap]

            # is the weight of this item > the current capacity?
            # and will including the current item lead to a better value compared to not including it?
            if cur_cap >= weight and take > drop:
                memory[i][cur_cap] = memory[i-1][cur_cap-weight] + value

    results = []
    cur_cap = C-1
    str_result = ""
    
    # backtrack the memory table to find the indices of the items we took
    for i in range(n-1, 0, -1):
        # if the item above this item is different, it means we took this item
        if memory[i][cur_cap] != memory[i-1][cur_cap]:
            results.append((items[i][2])-1)
            cur_cap = cur_cap - items[i][1]
    
    # build the string and print the result
    for i in range(len(results)-1, -1, -1):
        str_result += str(results[i]) + " "
    print(len(results))
    print(str_result)


# --- kattis

line = sys.stdin.readline()

while line:
    C, n = line.split()
    C = int(C)
    n = int(n)
    # items is a list of tuples, with value and weight. (0,0)
    items = [(0, 0, 0)]

    # the memory table, 2 x 2 array 
    memory = [[0 for i in range(C+1)] for j in range(n+1)]

    for i in range(1, n+1):
        value, weight = input().split()
        items.append((int(value), int(weight), i))

    # solve knapsack problem for the current knapsack
    solve(C+1, n+1, items, memory)

    # startover
    line = sys.stdin.readline()