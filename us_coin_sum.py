coins = [1, 5, 10, 25, 50]
def count(remainder):
	if remainder < 0:
		return 0
	if remainder == 0:
		return 1 
	return sum(count(remainder - coin) for coin in coins)
count(50)
