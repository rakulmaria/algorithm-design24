n = input()
n = int(n)

line = input().split()

line = map(int, line)

line = sorted(line, reverse=True)

c = 1
discount = 0

for ele in line:
    if c%3==0:
        discount+=ele
    c+=1

print(discount)