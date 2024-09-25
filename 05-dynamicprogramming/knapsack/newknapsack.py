import sys

def solve(sizes, values, C, n):
    for i in range(1, n+1):
        print(f"i: {i}")
        for c in range(C + 1):
            print(f"c: {c} C: {C}")
            if sizes[i] < c:
                memory[i][c] = memory[i - 1][c]
            elif memory[i - 1][c] > memory[i - 1][(sizes[i] + sizes[C])]:
                memory[i][c] = memory[i - 1][c]
            else:
                memory[i][c] = memory[i - 1][sizes[i] + values[i]]
    
    return memory[n][C]

line = sys.stdin.readline()

while line:
    C, n = line.split()
    C = int(C)
    n = int(n)
    # items is a list of tuples, with value and weight. (0,0)
    items = [(0, 0)]

    sizes = []
    values = []

    # the memory table, 2 x 2 array 
    memory = [[0 for i in range(C+1)] for j in range(n+1)]
    for i in range(1, n+1):
        value, weight = input().split()
        sizes.append(int(weight))
        values.append(int(value))
    
    print(f"values: {values}")
    print(f"sizes: {sizes}")
    print(f"memory: {memory}")
    res = solve(sizes, values, C, n)

    print(res)

    
    # startover
    line = sys.stdin.readline()