def naturals():
    i = 1
    while i:  #same as >>> while True:
        yield i
        i += 1

#錯誤的示範： 因為（1）Yield Outside the Loop:
#The yield elem statement is placed outside of the for loop.
#This means that the generator will only yield the last element, scaled,
# after the loop completes, rather than yielding each scaled element
#during each iteration of the loop.

#（2）Single Yield Statement：
#Because yield elem is outside the loop, the
#function does not behave as a generator that yields multiple values one-by-one.
#Instead, it completes the loop and
#then yields just one value, which is incorrect for the desired functionality.
"""
def scale(it, multiplier):
    for elem in it:
        elem = elem * multiplier

    yield elem
"""


def scale(it, multiplier):
     
    "*** YOUR CODE HERE ***"
    for elem in it:
        elem = elem * multiplier
        yield elem

def scale2(it, multiplier):
    """Alternative solution using yield from"""
    yield from map(lambda x: x * multiplier, it)


def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    yield n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n


def hailstone_recur(n): 
    """Alternative recursive solution"""
    yield n
    if n != 1:
        if n % 2 == 0:
            next_value = n // 2
        else:
            next_value = 3 * n + 1
        for value in hailstone_recur(next_value):
            yield value
            

    









































    
