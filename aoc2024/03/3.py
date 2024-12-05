import re
from sys import stdin

def solve1():
    regex =   r"mul\(\d{1,3},\d{1,3}\)"
    data = stdin.read()
    match = re.findall(regex, data)

    res = 0
    for muls in match:
        str = muls.strip("mul(").rstrip(")")
        a, b = str.split(",")
        res += int(a) * int(b)
    print(res)
    return res

def solve2():
    regex = re.compile(r"(mul\(\d{1,3},\d{1,3}\))*(do\(\))*(don't\(\))*")
    data = stdin.read()
    
    wait = False
    res = 0

    for match in regex.finditer(data):
        mul = match.group(1)
        do = match.group(2)
        dont = match.group(3)

        print(mul, do, dont)

        if dont != None:
            # we wait until we find do
            wait = True
            print(f"--- wait = {wait} ---")
        
        if do != None:
            wait = False
            print(f"--- wait = {wait} ---")
        
        if not wait and mul != None:
            print(f"--- wait = {wait} and mul = {mul} ---")
            # we calculate
            str = mul.strip("mul(").rstrip(")")
            a, b = str.split(",")
            res = res + (int(a) * int(b))
            print(f"res = {res}")

    print(res)
    return res

solve2()