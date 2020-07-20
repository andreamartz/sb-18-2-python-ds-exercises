def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    # complements = [num for num in nums if (goal-num) in nums]
    # already_visited = set()

    # lowest_index = len(complements)
    # for num in complements:
    #     index = complements.index(goal - num)
    #     if num not in already_visited and index < lowest_index:
    #         lowest_index = index
    #         result = tuple([num, goal - num])
    #     already_visited.add(num)
    #     already_visited.add(goal - num)
    # return result

    # ***************************
    # SB's SOLUTION
    # ***************************
    already_visited = set()

    for i in nums:
        difference = goal - i

        if difference in already_visited:
            return (difference, i)

        already_visited.add(i)

    return ()
