import random

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
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)    
    
    # # equivalent to above
    # if (a > 0 and b < 0):
    #     return True  
    # elif (a < 0 and b > 0):
    #     return True 
    # else:
    #     return False


def double_letters(text):
    """
    returns the string text with each character doubled

    >>> double_letters('hello')
    'hheelllloo'
    """
    doubled = ''
    for char in text:
        doubled += char*2
    return doubled

    # # equivalent using comprehensions
    # return ''.join([char*2 for char in text])

def random_element(a):
    """
    returns random element selected from list a
    """
    return random.choice(a)
    # return a[random.randint(0, len(a)-1)]

# def combine_lists(list1, list2):
#     """ 
#     returns combined list of alternating items

#     >>> combine_lists([1,2,3], [4,5,6])
#     [1, 4, 2, 5, 3, 6]
#     """
#     pass


def combine_lists_to_dict(keys, values):
    """ returns dict of keys zipped to values

    >>> combine_lists_to_dict(['a', 'b', 'c'], ['apples', 'bananas', 'cherries'])
    {'a': 'apples', 'b': 'bananas', 'c': 'cherries'}
    """
    return dict(zip(keys, values))


def eveneven(nums):
    """ returns if there is an even number of even numbers in num
    :num: list of ints

    >>> eveneven([5, 6, 2])
    True
    >>> eveneven([5, 5, 2])
    False
    """
    evens = [num for num in nums if num % 2 == 0] 
    return len(evens) % 2 == 0

    # evens = []
    # for num in nums:
    #     if num % 2 == 0:
    #         evens.append(num)
    # return len(evens) % 2 == 0


def powers_of_two(n):
    """ returns list of powers of 2 up to the nth power
    :n: int

    >>> powers_of_two(10)
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    """
    return [2**i for i in range(n)]


# scope example
# x = 0
# def looping():
#     x = 10  # local x 
#     print('x in func', x)
#     for x in range(10): # local x 
#         print('x in loop', x)
#     print('x in func', x)

# looping()
# print('x in main', x)