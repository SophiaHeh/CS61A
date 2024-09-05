def fib(n):
    
    pred = 1
    curr = 1
    k = 0
    while k < n :
        pred = curr 
        curr = pred + curr
        k = k + 1
    return curr 