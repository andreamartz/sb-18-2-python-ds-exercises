def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    return phrase[::-1]

    #========================================
    # THE LONG WAY!
    #========================================

    #****************************************
    # split the string into characters (returns a list?)
    #****************************************
    # phrase_list = list(phrase)

    #****************************************
    # iterate over the list in reverse order and create a new list
    #****************************************
    # index = len(phrase_list) - 1
    # phrase_list_reverse = []
    # while index >= 0:
    #     phrase_list_reverse.append(phrase_list[index])
    #     index -= 1
    #****************************************
    # join the characters back together & return
    #****************************************
    # return "".join(phrase_list_reverse)

