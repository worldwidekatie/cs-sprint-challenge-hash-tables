def get_indices_of_item_weights(weights, length, limit):

    cache = {}
    for i in range(length-1):
        for x in range(len(weights[i:])):
            if x != 0:
                cache[weights[i] + weights[i+x]] = (i+x, i)

    if limit in cache:
        return cache[limit]
    else:
        return None