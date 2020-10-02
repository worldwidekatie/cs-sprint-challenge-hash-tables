def has_negatives(a):
    # make a list for results to return
    result = []
    # make a list of positive integers
    pos = []
    # make a dictionary of negative integers
    cache = {}

    for i in a:
        # for each value, if it's negative, and not already
        # in the dictionary, turn it positive and add it.
        if i < 0 and i *-1 not in cache:
            cache[i *-1] = i *-1
        
        # otherwise it's positive so add it to postive
        else:
            pos.append(i)
    
    # now we can loop through just positive numbers and cut down on time
    for i in pos:
        # if it's in the dictionary, add it to results
        if i in cache:
            result.append(i)

    # return the result list
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
