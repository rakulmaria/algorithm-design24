from sys import stdin

def solve():
    n = int(stdin.readline())
    lst = list(map(int, stdin.readline().split()))
    dict = {}
    for ele in lst:
        x = dict.get(ele)
        if x != None:
            dict.update({ele : x + 1})
        else:
            dict.update({ele : 1})

    while True:
        if len(dict) == 0:
            return "none"
        current_largest = max(dict)
        if dict.get(current_largest) == 1:

            for i in range(len(lst)):
                if lst[i] == current_largest:
                    return i + 1
            #return current_largest, lst
        else:
            dict.pop(current_largest)

print(solve())