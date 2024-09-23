# made by @rakt, with inspiration from this website https://hideoushumpbackfreak.com/algorithms/algorithms-closest-pair.html

import math
import sys

def calc_dist(p1, p2):
    ax = p1[0]
    ay = p1[1]
    bx = p2[0]
    by = p2[1]
    return ((ax - bx) ** 2) + ((ay - by) ** 2)

def find_closest_pair(lst):
    # sort lst by x and y coordinate
    lst_x = sorted(lst)
    lst_y = sorted(lst, key=lambda y: y[1])

    return find_closet_pair_recursively(lst_x, lst_y)
    
    
def find_closest_pair_brute_force(lst):
    ''' naive approach, returns closest_pair in lst
    '''
    closest_distance = 98321397654
    closest_pair = ()

    for p1 in range(len(lst)):
        for p2 in range(len(lst)):
            if p1 != p2:
                dist = calc_dist(lst[p1], lst[p2])
                if dist < closest_distance:
                    closest_distance = dist
                    closest_pair = (lst[p1], lst[p2])

    return closest_pair, closest_distance

def find_closet_pair_recursively(lst_x, lst_y):
    ''' recursive approach, returns closets_pair in lst_x
    '''
    n = len(lst_x)
    closest_pair = ()

    if len(lst_x) < 3:
        return find_closest_pair_brute_force(lst_x)
    
    # divide the points down the middle of the x-axis
    mid = math.floor(n/2)
    left_cut = lst_x[:mid]
    right_cut = lst_x[mid:]

    # x value of the dividing point
    divide = lst_x[mid-1][0]

    # split y-sorted points into halves that match left-cut and right-cut
    left_y = []
    right_y = []

    for p in lst_y:
        if p[0] <= divide:
            left_y.append(p)
        else:
            right_y.append(p)

    left_closest_pair, delta1 = find_closet_pair_recursively(left_cut, left_y)
    right_closest_pair, delta2 = find_closet_pair_recursively(right_cut, right_y)

    closest_dist = min(delta1, delta2)
    

    if closest_dist == delta1:
        closest_pair = left_closest_pair
    else:
        closest_pair = right_closest_pair

    # create the strip
    strip = []

    for p in lst_y:
        if abs(p[0] - divide) <= closest_dist:
            strip.append(p)

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) <= closest_dist:
            dist = abs(calc_dist(strip[i], strip[j]))
            if dist < closest_dist:
                closest_dist = dist
                closest_pair = (strip[i], strip[j])
            j = j + 1

    return closest_pair, closest_dist





n = int(sys.stdin.readline())
lst = []

while n:
    p = []
    for _ in range(n):
        x, y = input().split()
        x = float(x)
        y = float(y)
        p.append((x, y))
    lst.append(p)
    n = int(sys.stdin.readline())

for point_lst in lst:
    points, dist = find_closest_pair(point_lst)
    sys.stdout.write(f"{points[0][0]} {points[0][1]} {points[1][0]} {points[1][1]}\n")