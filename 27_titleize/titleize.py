def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.split(" ")
    phrase_list = [f"{word.capitalize()}" for word in phrase]
    return " ".join(phrase_list)

    # *********************
    # SB's SOLUTION
    # *********************
    # there's a built-in method for this!

    # return phrase.title()

    # or, if you didn't know that, could capitalize each word by hand
    # return ' '.join([s.capitalize() for s in phrase.split(' ')])
