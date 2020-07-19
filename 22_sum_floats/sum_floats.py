def sum_floats(nums):
    """Return sum of floating point numbers in nums.

        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9

        >>> sum_floats([1, 2, 3])
        0
    """
    # ================================================
    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    # ================================================

    # filter out any list elements that are not floats
    # nums = [num for num in nums if isinstance(num, float)]

    # sum the remaining elements
    # sum = 0
    # for num in nums:
    #     sum = sum + num

    # return sum

    # ***********************
    # SB's SOLUTION
    # ***********************
    return sum([num for num in nums if isinstance(num, float)])
