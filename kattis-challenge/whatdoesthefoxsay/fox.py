# https://open.kattis.com/problems/whatdoesthefoxsay

from sys import stdin

def solve():
    sounds = stdin.readline().split()
    
    while True:
        line = stdin.readline().split()
        if line[0] == "what":
            # we want to print whatever sounds are left
            print(*sounds)
            return
        
        # else we want to filter out the animal sounds
        sounds = list(filter(lambda word: word != line[2], sounds))

T = int(stdin.readline())

for i in range(T):
    solve()