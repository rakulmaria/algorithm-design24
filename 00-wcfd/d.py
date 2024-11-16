import math

def solve():
    N = int(input())

    teamA = []
    teamB = []

    for i in range(N):
        a, b = map(int, input().split())
        teamA.append(a)
        teamB.append(b)
    
    prevA = teamA[0]
    prevB = teamB[0]
    whoseTurn = -1


    # edge case for the first line
    if abs(prevA - prevB) > 1:
        print("invalid v. 0")
        return
    for i in range(len(teamA)):
        if i == 0:
            if teamA[i]-1 <= 9 or teamB[i]-1 <= 9:
                print("invalid")
        while teamA[i] == teamB[i]:
            # nothing happens
        
            
solve()