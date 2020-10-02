
def finder(files, queries):
    # make a list of results to return
    result = []
    # make a dictionary for files
    cache = {}

    # go through each file
    for i in files:
        num = -1
        # check if the last character in the string is a /
        # if it's not, go too the next one to the left and check again
        while i[num] != "/":
            num -= 1
        x = i[num+1:]
        # When you have a window that includes everything before the first \
        # That string is the document so add it as the key to the cache
        if x not in cache:
            cache[x] = [i]
        # If it's already in the cache, add this new file path to the list
        else:
            cache[x].append(i)
    
    # go through all the file queries and look them up
    # in the cache dictionary
    for i in queries:
        # if it's in there, append everything in the value list to results
        if i in cache:
            for v in cache[i]:
                result.append(v)

    # return the result list
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
