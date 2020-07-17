def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # make a dictionary from the phrase
    phrase_dict = {}.fromkeys(phrase, 0)
    # iterate over the phrase
    for char in phrase:
        phrase_dict[char] += 1

    return phrase_dict

    # ***********************************
    # SPRINGBOARD's SOLUTION
    # ***********************************
    # start with an empty dictionary
    # counter = {}

    # iterate over the phrase:
    # for ltr in phrase:
    # If ltr is not a key in counter, make it a key and give it a value of 0. Otherwise, add 1 to the value of counter[ltr]
    # counter[ltr] = counter.get(ltr, 0) + 1

    # return counter
