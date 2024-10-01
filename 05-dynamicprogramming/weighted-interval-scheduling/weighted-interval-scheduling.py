from sys import stdin


def solve():
    # kattis - read input
    n = int(stdin.readline())
    intervals = []

    for _ in range(n):
        start, end, weight = map(int, stdin.readline().split())
        intervals.append((start, end, weight))

    # sort intervals by finish time
    intervals.sort(key=lambda x: x[1])

    # instantiate memoization table
    M = [0 for i in range(n)]

    # set the first interval
    M[0] = intervals[0][2]

    # solve the maximum value from 1 to n 
    # and fill in the memoization table
    for i in range(1, n):
        val = intervals[i][2]
        p = compute_p(intervals, i)

        if p != -1:
            val += M[p]

        M[i] = max(val, M[i-1])


    # print the result
    print(M[n-1])


# compute p[n] using binary search
def compute_p(intervals, start):
    low = 0
    high = start - 1

    # perform binary search to compute p[n]
    while low <= high:
        mid = (low + high) // 2
        if intervals[mid][1] <= intervals[start][0]:
            if intervals[mid + 1][1] <= intervals[start][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    
    # if no job before index conflicts, returns -1
    return -1


solve()