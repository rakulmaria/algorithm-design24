import sys

def opt():
    # kattis setup
    C = 1000
    n = int(sys.stdin.readline())

    weights = [0]
    memory = [[0 for i in range((C*2)+1)] for j in range(n+1)]

    for _ in range(n):
        weights.append(int(sys.stdin.readline()))
    
    # --- algorithm starts 
    for row in range(0, len(memory)):
        weight = weights[row] 
        
        for col in range(len(memory[0])):
            # check if we have room for the current item
            if weight > col:
                continue
            # check the item directly above this item and see what is best
            else:
                item_above = memory[row-1][col]
                current_item = weight + memory[row-1][col - weight]
                
                if item_above < current_item:
                    memory[row][col] = current_item
                else:
                    memory[row][col] = item_above


    # check what the value at capacity = 1000 is and compare it to the next value
    initial_val = memory[n][C]
    for i in range(C+1, len(memory[n])):

        if memory[n][i] == initial_val:
            continue
        # else check what number is closest to 1000
        # 1002
        else:
            if abs(C - memory[n][i]) <= abs(C - initial_val):
                initial_val = memory[n][i]
                break

    print(f"{initial_val}")

opt()