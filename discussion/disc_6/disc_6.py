# Q1_page2

def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n


    return f
#page 5
    """def mystery(p, q):
        p[1].extend
    """

#page 6 question
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    #check each element in the list that return the same value from fn(e)
    #group them in a list to assign to repective key of dictionaries
            
    grouped = {}
    for e in s:
        key = fn(e)
        if key in grouped:
            grouped[key].append(e)
        else:
            grouped[key] = [e]

    return grouped
            
#page 7 question
def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    # check the number of times x occurs in s
    # append el at the respective number times in s
    # return s
    num = 0
    for i in range(len(s)):
        if s[i] == x:
            num += 1
    for i in range(1, num + 1):
        s.append(el)

    return s
#alternative solution:
"""
def add_this_many(x, el, s):
    for i in range(len(s)):
        if s[i] == x:
            s.append(el)
"""


def gen_naturals():
    current = 0
    while True:
        yield current
        current += 1
        
#page 11
def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for x in iterable:
        if fn(x):
            yield x

# page12
def merge(a, b):
    """
    >>> def sequence(start, step):
    ... while True:
    ... yield start
    ... start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    #for x in a:
    #    for y in b:
    #        if x == y:
    #            yield x
    #        else:
    #            yield min(x, y)
    #            yield max(x, y)
    """
    next_a = next(a)
    next_b = next(b)
    while True:
        if next(a) == next(b):
            yield next_a
            next_a = next(a)
            next_b = next(b)
            
        else:
            yield min(next_a, next_b)
            yield max(next_a, next_b)
            next_a = next(a)
            next_b = next(b)
    """
    next_a, next_b = next(a), next(b)
    while True:
        if next_a == next_b:
            yield next_a
            next_a, next_b  = next(a), next(b)
            
        elif next_a < next_b:
        
            yield next_a
            next_a = next(a)
        else:
            yield next_b
            next_b = next(b)
    
    
def sequence(start, step):
    while True:
        yield start
        start += step

        




