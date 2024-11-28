# https://open.kattis.com/problems/yoda
from sys import stdin

N = stdin.readline().replace("\n", "")
M = stdin.readline().replace("\n", "")

N = list(reversed(N))
M = list(reversed(M))

if len(N) < len(M):
    dif = len(M) - len(N)
    for n in range(dif):
        N.append(0)
elif len(M) < len(N):
    dif = len(N) - len(M)
    for n in range(dif):
        M.append(0)

result_n = []
result_m = []

for j in range(len(N)):
    current_n = int(N[j])
    current_m = int(M[j])

    if current_m == current_n:
        result_n.append(current_n)
        result_m.append(current_n)

    if current_n < current_m:
        result_m.append(current_m)

    if current_m < current_n:
        result_n.append(current_n)

if len(result_n) == 0:
    res_n = "YODA"

elif all(v == 0 for v in result_n):
    res_n = 0

else:
    result_n.reverse()
    res_n = "".join(map(str, result_n))

if len(result_m) == 0:
    res_m = "YODA"

elif all(v == 0 for v in result_m):
    res_m = 0

else:
    result_m.reverse()
    res_m = "".join(map(str, result_m))

print(res_n)
print(res_m)
