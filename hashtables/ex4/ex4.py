def has_negatives(a):
    result = []
    pos = []
    cache = {}

    for i in a:
        if i < 0 and i *-1 not in cache:
            cache[i *-1] = i *-1
        else:
            pos.append(i)
    
    for i in pos:
        if i in cache:
            result.append(i)


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
