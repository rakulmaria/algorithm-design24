from sys import stdin

lands = []

for i in range(8):
    name, area, price = stdin.readline().split(", ")
    price = int(price)
    lands.append((name, price))

lands = sorted(lands, key=lambda ele: ele[1])


C = 1000
res = []

for ele in lands:
    thisPrice = ele[1]
    if C - thisPrice >= 0:
        res.append(ele[0])
        C = C - thisPrice
    
print(*res, sep="\n")
    
