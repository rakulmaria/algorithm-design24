word = input().split()
sol = ""

for c, i in enumerate(word):
    cur = word[i]
    print(cur)
    if cur == "<":
        word[i] = ""

print(word)

