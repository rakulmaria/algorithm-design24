import random

file = open('10.in', 'w')

C, n = input().split()
C = int(C)
n = int(n)

file.write(str(C) + " " + str(n) + "\n")

for _ in range(n):
    v = random.randrange(1, 10000)
    w = random.randrange(1, C)

    file.write(str(v) + " " + str(w) + "\n")
