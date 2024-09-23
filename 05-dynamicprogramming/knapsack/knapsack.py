import numpy as np
import sys

def print_memory(memory):
    for n in range(len(memory[0])):
        print(f"|  {n} |", end='')

    print("")
    for n in range(len(memory[0])):
        print("*----*", end='')

    for i in range(len(memory)):
        print("")
        for j in range(len(memory[0])):
            print(f"| {memory[i][j]} |", end='')

    print("")

def opt(i, c):
    if i == 0:
        return 0
    if items[i][1] > c:
        return opt(i-1, c)
    else:
        drop = opt(i-1, c)
        take = items[i][0] + opt(i - 1, c - items[i][1])
        memory[i][c] = take
        return max(drop, take)


# backtrack memory array
def res(n, C):
    res = []
    
    for i in range(n, 0, -1):  # Backtrack from the last item
        if memory[i][C] != memory[i - 1][C]:
            # Item i-1 is included in the optimal solution
            res.append(i-1)  # Store the index of the item
            C -= items[i-1][1]  # Reduce the capacity by the item's weight

    return res


line = sys.stdin.readline()

while True:
    if line:
        print("\n--- new knapsack ---")
        C, n = line.split()
        C = int(C)
        n = int(n)
        print(f"Capacity: {C} Items: {n}")
        
        # items is a list of tuples, with value and weight
        items = np.zeros(n+1, tuple)
        # the memory table, 2 x 2 array 
        memory = np.full((n + 1, C + 1), -1)

        items[0] = (0, 0)
        for i in range(1,n+1):
            value, weight = input().split()
            items[i] = (int(value), int(weight))

        # solve the knapsack problem for this current knapsack
        opt(n, C)
        #print(memory)

        result = res(n, C)
        print(len(result))
        for i in range(len(result) - 1, -1, -1):
            print(result[i], end=' ')
        
        #start over
        line = sys.stdin.readline()

    else:
        break

