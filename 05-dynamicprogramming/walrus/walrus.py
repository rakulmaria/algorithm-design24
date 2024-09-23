import numpy as np
import sys

def closest_to_1000(n, m):
    print(f"comparing {n} with {m}")
    if n == 0:
        return m
    if m == 0:
        return n
    if abs(1000 - n) < abs(1000 - m):
        print(f"closest to 1000: {n}")
        return n
    else:
        print(f"closest to 1000: {m}")
        return m

def opt(i, c):
    print(f"checking optimal solution of w[{i}]: {weights[i]} with c: {c}")
    w = weights[i]
    if i == 0:
        return 0
    if weights[i] > c:
        return opt(i-1, c)
    # opt of the previous item with this weight
    drop = opt(i-1, c)

    # opt of this item + opt prev solution
    take = (w + opt(i-1, c-w))

    # what res is closest to 1000
    res = closest_to_1000(drop, take)

    memory[i][c] = res

    return res




n = int(sys.stdin.readline())
C = 2000

weights = np.zeros(n+1, int)
memory = np.full((n + 1, C + 1), 0)

print(f"{len(memory[0])} x {len(memory)}")

for i in range(1,n+1):
    weights[i] = int(sys.stdin.readline())


print(f"weights: {weights}")
opt(n, C)

for row in range(len(memory)):
    print(memory[row].max())

