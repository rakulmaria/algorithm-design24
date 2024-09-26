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
        for item in range(len(memory)):
            # we just want 0s on the first row
            if item == 0:
                continue

            # take the value and weight of the item that we want to place in this row
            cur_value, cur_weight = items[item][0], items[item][1]

            for capacity in range(len(memory[0])):
                # we also just want 0s on the first column
                if capacity == 0:
                    continue
                
                # we don't have space for this item, so we continue increasing the capacity
                if capacity < cur_weight:
                    memory[item][capacity] = memory[item-1][capacity]
                    continue

                # we have room - time for checking
                else:
                    # get the value from the item directly above the current item
                    val_item_above = memory[item-1][capacity]
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
        i = len(memory)-1
        cap = len(memory[0])-1
        indices = []
        current_item = memory[i][cap]

        while True:
            # we found all the items from our memory table
            if current_item == 0:
                break
            above_item = memory[i-1][cap]
           
            if current_item != above_item:  # it means that we took the current item
                indices.append(i-1) # i is not 0 indexed
                current_item = memory[i-1][cap - items[i][1]]
                
                cap -= items[i][1]
                i -= 1
                total_items += 1
            else: # we didn't take this item so look one up
                i -= 1
                current_item = memory[i][cap]

        print(total_items)
        print(*indices)
        # startover
        line = sys.stdin.readline()
#start_time = time.time()
solve()
#print("--- %s seconds ---" % (time.time() - start_time))