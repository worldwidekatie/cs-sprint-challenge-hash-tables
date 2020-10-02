def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    nums = {}
    
    for i in arrays:
        for num in i:
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] += 1

    for i in nums:
        if nums[i] == len(arrays):
            result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
