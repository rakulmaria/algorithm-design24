from sys import stdin

N = int(stdin.readline())

if N <= 7:
    if N == 2:
        print(28)
    elif N % 2 == 1:
        print(31)
    else:
        print(30)
elif N >= 8:
    if N % 2 == 1:
        print(30)
    else:
        print(31)