import sys


file = open('4.in', 'w')
N = int(sys.stdin.readline())
file.write(str(N)+"\n")

for i in range(1,N+1):
    n = i * 2
    file.write(str(n)+"\n")

