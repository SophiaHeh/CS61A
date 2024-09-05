def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) 
    1
    >>> sum_digits(4224) 
    12
    >>> sum_digits(1234567890)
    45
    """
    ans = 0
    while y > 0:
        last_digit = y % 10
        ans += last_digit
        y = y // 10
    return ans
