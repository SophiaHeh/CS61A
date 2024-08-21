def count_k(n, k):
	if  n == 0: 
		return 1
	elif n < 0:
		return 0
	elif k <= 0:
		return 0
	else: 
		with_k_steps = count_k(n-k, k) 
		without_k_steps = count_k(n, k-1) 
		return with_k_steps + without_k_steps
	    

"""n == 0 代表,沒有數字要被組成，就是什麼都不用做(do nothing)，這個是“一種”可能
N < 0  represent something wrong and we return 0 because we are not allowed to use negative number in this case.

m <= 0 there is no way to build anything out of zero steps so we return zero.
"""
