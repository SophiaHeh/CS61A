def count_k(n, k):
    """
    Return the number of different ways to climb a flight of stairs with n steps,
    where you can take up to and including k steps at a time.

    >>> count_k(3, 3)  # 3, 2 + 1, 1 + 2, 1 + 1 + 1 4
    4
    >>> count_k(4, 4)  # 1 + 1 + 1 + 1, 2 + 1 + 1, 1 + 2 + 1, 1 + 1 + 2, 3 + 1, 1 + 3, 2 + 2, 4
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)  # Only one step at a time
    1
    """
    if n == 0:
        return 1  # Base case: If there are 0 steps, there is only 1 way to climb (by doing nothing).
    elif n < 0:
        return 0  # Base case: If there are negative steps, there are no ways to climb.
    else:
        total = 0
        for step in range(1, min(k, n) + 1):
            total += count_k(n - step, k)
        return total



