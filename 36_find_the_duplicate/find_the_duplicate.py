def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # create an empty list:  checked_nums = []
    # loop thru the list
    # for each num, if it's not in checked_nums, add it.  If it is in there, that's the dupe

    checked_nums = []

    for num in nums:
        if checked_nums.count(num) > 0:
            return num
        if checked_nums.count(num) == 0:
            checked_nums.append(num)
    return None
