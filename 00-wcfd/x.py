n = int(input())

a, b = 10, 10

playerAShoots = True
gameStarted = False
firstShot = True


for i in range(n):
    x, y = map(int, input().split(' '))
    if (a == 0 or b == 0):
        print("invalid")
        exit(0)
    
    if firstShot:
        if x == 9 and y == 10:
            playerAShoots = False
            gameStarted = True
        elif x == 10 and y == 9:
            playerAShoots = True
            gameStarted = True
        elif x+y != 20:
            print("invalid")
            exit(0)
        firstShot = False
        a, b = x, y
    else:
        # Points can now be up to 2
        if gameStarted:    
            if playerAShoots:
                if not ((x == a or x == a-1 or x == a-2) and y == b):
                    # game is invalid
                    print("invalid")
                    exit(0)
            else:
                if not ((y == b or y == b-1 or y == b-2) and x == a):
                    # game is invalid
                    print("invalid")
                    exit(0)
        elif (a != x or b != y) and (x == 10 or y == 10):
            playerAShoots = a != x
            gameStarted = True
        a, b = x, y
        playerAShoots = not playerAShoots

if a == 0 or b == 0:
    print("finished")
else:
    print("ongoing")
