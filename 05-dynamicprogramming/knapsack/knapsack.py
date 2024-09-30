import sys
#import time

def solve():
    while True:
        try:
            line = sys.stdin.readline()
            if line == "":
                break
        except:
            break
    
        C, n = line.split()
        C = int(C)
        n = int(n)

        values = [0]
        weights = [0]
        

        # the memory table, 2 x 2 array 
        memory = [[0 for i in range(C+1)] for j in range(n+1)]

        for i in range(n):
            value, weight = input().split()
            values.append(int(value))
            weights.append(int(weight))

        # fill in the memory table
        for item in range(1, n+1):

            # take the value and weight of the item that we want to place in this row
            cur_value = values[item]
            cur_weight = weights[item]

            for capacity in range(1, C+1):

                # get the value from the item directly above the current item
                val_item_above = memory[item-1][capacity]

                # we don't have space for this item, so we take the above capacity
                if capacity < cur_weight:
                    memory[item][capacity] = val_item_above

                # we have room - time for checking
                else:
                    memory[item][capacity] = max(cur_value + memory[item-1][capacity - cur_weight], val_item_above)
                
        # now we want to backtrack our memory table and find the number of items taken and their indices
        indices = []
        current_item = memory[n][C]

        while True:
            if n == 0:
                break

            current_item = memory[n][C]
            above_item = memory[n - 1][C]

            if current_item != above_item:
                indices.append(n - 1)
                C -= weights[n]
            
            n -= 1

        print(len(indices))
        print(*indices)
#start_time = time.time()
solve()
#print("--- %s seconds ---" % (time.time() - start_time))