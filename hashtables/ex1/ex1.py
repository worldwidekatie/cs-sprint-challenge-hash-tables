def get_indices_of_item_weights(weights, length, limit):
    # First made an array to store everything in
    cache = {}

    # Then populate that array with all the possible combinations
    # with sum as they key
    # Start with the first item but don't go all the way to the last.
    for i in range(length-1):
        # Go through the rest of the list after your current item
        for x in range(len(weights[i:])):
            if x != 0:
                # Make the sum of current item and next item your key
                # And add the tuple of their index numbers as the value.
                cache[weights[i] + weights[i+x]] = (i+x, i)

    # Check if any of them added up to the limit
    # if so, return that tuple.
    if limit in cache:
        return cache[limit]

    # Or else return None    
    else:
        return None