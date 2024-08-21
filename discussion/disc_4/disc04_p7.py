def max_product(s):
	
    if  len(s) ==  0:
        return 1
    elif len(s) == 1 :
        return s[0]
    else:
        return max(s[0] * max_product(s[2:]), max_product(s[1:]))



#Redundant Condition: Checking len(s) < 0 is unnecessary
#because the length of a list cannot be negative.
#Therefore, this condition is redundant and can be removed.
