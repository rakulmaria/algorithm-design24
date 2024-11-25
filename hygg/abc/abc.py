from sys import stdin

nums = sorted(list(map(int, stdin.readline().split())))
dict = {"A" : nums[0], "B" : nums[1], "C": nums[2]}
order = list(stdin.readline().strip())

for o in order:
    print(dict.get(o), end=" ")