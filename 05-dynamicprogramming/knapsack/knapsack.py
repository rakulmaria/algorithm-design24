import sys
#import time

def solve():
    # --- kattis
    line = sys.stdin.readline()

    while line:
        C, n = line.split()
        C = int(C)
        n = int(n)

        # items is a list of tuples, with value and weight. (0,0)
        items = [(0, 0)]
        

        # the memory table, 2 x 2 array 
        memory = [[0 for i in range(C+1)] for j in range(n+1)]

        for i in range(1, n+1):
            value, weight = input().split()
            items.append((int(value), int(weight)))

        # fill in the memory table
        for item in range(n+1):
            # we just want 0s on the first row
            if item == 0:
                continue

            # take the value and weight of the item that we want to place in this row
            cur_value, cur_weight = items[item][0], items[item][1]

            for capacity in range(C+1):
                # we also just want 0s on the first column
                if capacity == 0:
                    continue

                # get the value from the item directly above the current item
                val_item_above = memory[item-1][capacity]
                # we don't have space for this item, so we continue increasing the capacity
                if capacity < cur_weight:
                    memory[item][capacity] = val_item_above
                    continue

                # we have room - time for checking
                else:
                    # and compute the value that we get from taking this item
                    val_current_item = cur_value + memory[item-1][capacity - cur_weight]

                    # taking the current item is better than the one directly above it
                    if val_item_above < val_current_item:
                        memory[item][capacity] = val_current_item 
                    # otherwise taking the item above is better than taking this one
                    else:
                        memory[item][capacity] = val_item_above

        # now we want to backtrack our memory table and find the number of items taken and their indices
        total_items = 0
        indices = []
        current_item = memory[n][C]

        while True:
            # we found all the items from our memory table
            if current_item == 0:
                break
            above_item = memory[n-1][C]
            new_C = items[n][1]
           
            if current_item != above_item:  # it means that we took the current item
                indices.append(n-1) # i is not 0 indexed
                current_item = memory[n-1][C - new_C]
                
                C -= new_C
                n -= 1
                total_items += 1
            else: # we didn't take this item so look one up
                n -= 1
                current_item = memory[n][C]

        print(total_items)
        print(*indices)
        # startover
        line = sys.stdin.readline()
#start_time = time.time()
solve()
#print("--- %s seconds ---" % (time.time() - start_time))