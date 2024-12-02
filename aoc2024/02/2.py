from sys import stdin

def check_increase(lst):
    prev = lst[0]
    safe = True

    for i in range(1, len(lst)):
        cur = lst[i]
        if prev >= cur:
            safe = False

        if abs(prev - cur) > 3 or prev == cur:
            safe = False
            
        prev = cur
    
    return safe

def check_decrease(lst):
    prev = lst[0]
    safe = True

    for i in range(1, len(lst)):
        cur = lst[i]
        if prev <= cur:
            safe = False
        if abs(prev - cur) > 3 or prev == cur:
            safe = False
        
        prev = cur
    
    return safe

def remove_level(lst, isIncreasing):
    safe = False

    for i in range(len(lst)):
        ele = lst.pop(i)

        if check_increase(lst):
            return True

        if check_decrease(lst):
            return True
        
        if not safe:
            lst.insert(i, ele)
        
        if safe:
            return safe
        
    return safe


def solve1():
    data = stdin.read().splitlines()
    safe = True
    res = 0
    
    for line in data:
        lst = list(map(int, line.split()))
        
        if lst[0] < lst[1]:
            increasing = True
        else:
            increasing = False

        if increasing:
            # all elements must increase
            safe = check_increase(lst)

        if not increasing:
            # all elements must decrease
            safe = check_decrease(lst)

        if not safe:
            # remove some level
            safe = remove_level(lst, increasing)
            
        if safe:
            res += 1
    
    print(res)


solve1()