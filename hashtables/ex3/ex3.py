def intersection(arrays):
    # make the result list to return
    result = []
    # make the dict to become all the numbers in all the lists
    nums = {}
    
    # loop through each list in the given list
    for i in arrays:
        # loop through each number in said list
        for num in i:
            # if it's not in nums already, add it and one count
            if num not in nums:
                nums[num] = 1
            # if it's already in nums, add one to the value/count
            else:
                nums[num] += 1
    
    # go through the whole nums dictionary
    for i in nums:
        # if the count for a key is equal to the number of lists given,
        # the number was in every list so add it to results.
        if nums[i] == len(arrays):
            result.append(i)
    
    # Return the result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
