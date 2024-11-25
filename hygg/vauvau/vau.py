from sys import stdin

def solve():
    def helper(n):
        if dog1[n] and dog2[n]:
            return "both"
        if not dog1[n] and not dog2[n]:
            return "none"
        else:
            return "one"
        
    a, b, c, d = map(int, stdin.readline().split())
    P, M, G = map(int, stdin.readline().split())

    dog1 = []
    dog2 = []

    for i in range(1, a+1):
        dog1.append(True)
    for i in range(a+1, a+b+1):
        dog1.append(False)

    for i in range(1, c+1):
        dog2.append(True)
    for i in range(c+1, c+d+1):
        dog2.append(False)

    while len(dog1) < 999:
        dog1.extend(dog1)
        dog2.extend(dog2)

    print(helper(P-1))
    print(helper(M-1))
    print(helper(G-1))

solve()