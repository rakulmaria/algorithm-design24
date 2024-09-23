def gale_shapley(n, proposers, rejectors):
    matches = {}
    
    while len(matches) < n // 2:
        for proposer in proposers:
            # if proposer is already matched, skip
            if proposer in matches:
                continue
            
            # get the first priority of this proposers match
            for rejector in proposers.get(proposer):
                # if rejector is unmatched
                if rejector not in matches.values():
                    # match the proposer with the rejector
                    matches[proposer] = rejector
                    # remove the rejector from the proposers list
                    proposers.get(proposer).remove(rejector)
                    break
                else:
                    # check if rejector prefers new partner to previous partner
                    previouspartner = list(matches.keys())[list(matches.values()).index(rejector)] # stackoverflow

                    # find the rank of previous partner
                    lst = rejectors.get(rejector)

                    ppRank = -1
                    nmRank = -1

                    for i in range(len(lst)):
                        if lst[i] == previouspartner:
                            ppRank = i
                        elif lst[i] == proposer:
                            nmRank = i

                    # compare the two partners rank, the smaller one wins
                    if ppRank > nmRank:
                        # print("previous rank:", ppRank, "newpartner rank:", nmRank)
                        # update to match with the new partner
                        matches.pop(previouspartner)
                        matches[proposer] = rejector
                        proposers.get(proposer).remove(rejector)
                        break
                    else:
                        continue

    for (r, p) in matches.items():
        print(r, p)

## code starts here

n, m = input().split()
n = int(n)
m = int(m)

proposers = {}
rejectors = {}

for i in range(n):
    if i < n // 2:
        # add to proposers
        line = input().split()
        proposers[line[0]] = line[1:]
    else:
        # add to rejectors
        line = input().split()
        rejectors[line[0]] = line[1:]

gale_shapley(n, proposers, rejectors)
