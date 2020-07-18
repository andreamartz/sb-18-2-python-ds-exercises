def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # iterate over the phrase
    # for every char that matches to_swap,
    # change the case of that char using str.swapcase()

    idx = 0
    phrase_list = list(phrase)
    while idx < len(phrase_list):
        if phrase_list[idx] == to_swap.lower() or phrase_list[idx] == to_swap.upper():
            phrase_list[idx] = phrase_list[idx].swapcase()
        idx += 1
    phrase = "".join(phrase_list)
    return phrase

    # ****************************************
    # SB's SOLUTION
    # ****************************************
    # to_swap = to_swap.lower()
    # out = ""

    # for ltr in phrase:
    #     if ltr.lower() == to_swap:
    #         ltr = ltr.swapcase()
    #     out += ltr

    # return out
