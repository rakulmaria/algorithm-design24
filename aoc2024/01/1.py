from sys import stdin

def solve1():
    data = stdin.read().splitlines()
    lst1 = []
    lst2 = []

    for i in data:
        n, m = map(int, i.split())
        lst1.append(n)
        lst2.append(m)

    lst1.sort()
    lst2.sort()

    res = 0

    for i in range(len(lst1)):
          res += abs(lst1[i] - lst2[i])

    print(res)

def solve2():
    data = stdin.read().splitlines()
    lst = []
    map2 = {}

    for i in data:
        n, m = map(int, i.split())

        lst.append(n)
        y = map2.get(m)
        
        if y != None:
            map2.update({m : y + 1})
        else:
            map2.update({m : 1})

    res = 0

    for ele in lst:
        x = map2.get(ele)
        if x != None:
            res += ele * x

    print(res)

          

#solve1()
solve2()