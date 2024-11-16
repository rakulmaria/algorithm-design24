a, b = input.split()

# if a = 2 it's always now
if a == 2:
    print("no")

# if a == 3 and b == even: no b == uneven: yes
if a == 3:
    if b % 2 == 0:
        print("no")
    else:
        print("yes")

    