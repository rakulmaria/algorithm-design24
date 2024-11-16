
N = int(input())

str0 = "  "
for i in range(N):
    str0 += "H "

str0 += " "

str1 = "  "
for i in range(N):
    str1 += "| "

str1 += " "

str2 = "H-"
for i in range(N):
    str2 += "C-"

str2 += "OH"

print(str0)
print(str1)
print(str2)
print(str1)
print(str0)