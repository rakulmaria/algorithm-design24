import random

file = open('10.in', 'w')

n = int(input())

file.write(str(n) + "\n")

for _ in range(n):
    s = random.randrange(0, 10)
    f = random.randrange(10, 20)
    w = random.randrange(1, 5)

    file.write(str(s) + " " + str(f) + " " + str(w) + "\n")
