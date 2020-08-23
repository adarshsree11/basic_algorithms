#fibanocci series in recursive approach
def fibanocci(n):
	if n==1 or n==2:
		return 1
	else:
		result = fibanocci(n-1)+fibanocci(n-2)
		return result

#fibanocci series in memoized approach
def fibanocci_memo(n, memo):
	if memo[n] is not None:
		return memo[n]
	if n==1 or n==2:
		return 1
	else:
		result = fibanocci_memo(n-1, memo)+fibanocci_memo(n-2, memo)
		memo[n] = result
		return result

#fibanocci series in bottom_up approach
def fibanocci_bottom_up(n):
	if n==1 or n==2:
		return 1
	bottom_up = [None]* (n+1)
	bottom_up[1] = 1
	bottom_up[2] = 1

	for i in range(3, n+1):
		bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
	return bottom_up[n]


if __name__ == '__main__':
	on = True
	while on:
		approach = int(input("1.recursive\n2.memoized\n3.back_up\n4.exit\n"))
		if approach == 1:
			value = int(input("fibanocci number at : "))
			print(fibanocci(value))
		elif approach == 2:
			value = int(input("fibanocci number at : "))
			memo = [None]*(value+1)
			print(fibanocci_memo(value, memo))
		elif approach == 3:
			value = int(input("fibanocci number at : "))
			print(fibanocci_bottom_up(value))
		else:
			on = False
