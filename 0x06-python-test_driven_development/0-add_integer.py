#!/usr/bin/python3
def add_integer(a, b):
    """Returns the sum of two integers or floats"""
    if not isinstance(a, int) and not isinstance(a, float) or \
       isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float) or \
       isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
