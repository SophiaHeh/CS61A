def count_stair_ways(n):
    if n == 1:
        return 1
    elif n == 2:  #easy to froget this base case
        return 2
    else:
        count_stair_ways(n - 1) + count_stair_ways(n - 2)
