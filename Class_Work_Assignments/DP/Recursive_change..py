import math
def recurse_change(money,coins):
	if money==0:
		return 0
	min_coins=math.inf
	for i in coins:
		if money>=i:
			min=1+recurse_change(money-i,coins)
			if min_coins>min:
				min_coins=min
	return min_coins

coins=[6,5,1]
print(recurse_change(40,coins))