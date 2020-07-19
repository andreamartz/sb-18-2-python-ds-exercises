def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # return isinstance(lst[0], list)
    # bool_list = [isinstance(elem, list) for elem in lst]
    # if len(set(bool_list)) != 1:
    #     return False
    # else:
    #     return True

    # BETTER:
    # bool_list = [isinstance(elem, list) for elem in lst]
    # if all(bool_list):
    #     return True
    # else:
    #     return False

    # BEST:
    return all(isinstance(elem, list) for elem in lst)
