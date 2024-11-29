from sys import stdin

N = int(stdin.readline())

previousWord = stdin.readline().strip()
res = 0

for i in range(N - 1):
    currentWord = stdin.readline().strip()

    if currentWord == "sober" and previousWord == "drunk":
        res = res + 1

    previousWord = currentWord


print(res)