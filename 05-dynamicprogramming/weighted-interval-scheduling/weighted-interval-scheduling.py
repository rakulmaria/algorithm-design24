from sys import stdin


def opt(j):
    if j == 0:
        return 0
    
    if M[j] != -1:
        return M[j]
    else:
        M[j] = max((lst[j][2] + opt(p(j)), opt(j - 1)))
        return M[j]


def p(n):
    cur = lst[n]
    
    match = False
    for j in range(n-1, 0, -1):
        prev = lst[j]
        # if the previous start time is before the previous end time it's not a match
        if cur[0] < prev[1]:
            continue
        else:
            match = True
            return j
    if not match:
        return 0


n = int(stdin.readline())
lst = [(0, 0, 0)]

for _ in range(n):
    start, end, weight = map(int, stdin.readline().split())
    lst.append((start, end, weight))

# sort lst by finish-time
lst.sort(key=lambda x: x[1])

M = [-1 for i in range(n+1)]

print(opt(n))