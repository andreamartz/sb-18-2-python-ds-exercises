def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # make the phrase all lowercase and remove internal spaces
    phrase = phrase.lower().replace(" ", "")
    # create a new string phrase_reversed
    phrase_reversed = phrase[::-1]
    # determine whether phrase has the same contents and order as phrase_reversed
    return phrase == phrase_reversed

    # ****************************************
    # SB's SOLUTION IS SIMILAR
    # ****************************************
    # normalized = phrase.lower().replace(' ', '')
    # return normalized == normalized[::-1]
