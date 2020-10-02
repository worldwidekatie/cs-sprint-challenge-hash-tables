
def finder(files, queries):
    result = []
    cache = {}
    for i in files:
        num = -1
        while i[num] != "/":
            num -= 1
        x = i[num+1:]
        if x not in cache:
            cache[x] = [i]
        else:
            cache[x].append(i)
    for i in queries:
        if i in cache:
            for v in cache[i]:
                result.append(v)

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
