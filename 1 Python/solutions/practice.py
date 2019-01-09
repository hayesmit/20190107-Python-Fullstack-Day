def is_even(a):
    """ returns if number is even

    >>> is_even(1)
    False
    >>> is_even(2)
    True
    """
    return a%2 == 0
    
    # # equivalent to above
    # if a%2 == 0:
    #     return True 
    # else: 
    #     return False


def opposite(a, b):
    """ returns if a and b have opposite polarity
    
    >>> opposite(1, -1)
    True
    >>> opposite(-1, 0)
    True
    >>> opposite(-1, -9)
    False
    >>> opposite(2, 3)
    False
    """
    return (a > 0 and b < 0) or (a < 0 and b > 0)    
    
    # # equivalent to above
    # if (a > 0 and b < 0):
    #     return True  
    # elif (a < 0 and b > 0):
    #     return True 
    # else:
    #     return False