from sys import stdin

line = list(stdin.readline())
line = [x.lower() for x in line]
i = 0

for ele in line:
    if ele == 'a' or ele == 'e' or ele == 'i' or ele == 'o' or ele == 'u':
        i = i + 1

print(i)