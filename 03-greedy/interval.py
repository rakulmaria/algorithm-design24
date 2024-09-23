n = input()
n = int(n)

J = []

for i in range(n):
    s, f = input().split()
    s = int(s)
    f = int(f)
    J.append((s, f))

J = sorted(J, key=lambda ele: ele[1])

non_overlapping_integers = 1
prev_finishtime = J[0][1]

for ele in J[1:]:
    cur_starttime = ele[0]
    if prev_finishtime <= cur_starttime:
        non_overlapping_integers+=1
        prev_finishtime = ele[1]

print(non_overlapping_integers)