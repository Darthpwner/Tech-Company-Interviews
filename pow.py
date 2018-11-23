
# Time complexity: O(a * b)
# Space complexity: O(a) where a is the base you are raising to

def recursivePow(a, b):
	if b < 0.0:
		return None

	if b == 0.0:
		return 1.0
	elif b == 1.0:
		return a

	expression = 0
	for i in range(0, a):
		expression += recursivePow(a, b - 1)

	return expression

print(recursivePow(2, 20))

recursiveMemo = {0: 1}
def memoizedRecursivePow(a, b, memo):
	if b < 0.0:
		return None

	if 1 not in memo:
		memo[1] = a

	if b in memo:
		return memo[b]

	else:
		memo[b] = 0
		for i in range(0, a):
			memo[b] += memoizedRecursivePow(a, b - 1, memo)

		print(memo)
		return memo[b]

memoizedRecursivePow(2, 20, recursiveMemo)

# Time complexity: O(log b) where b is the power you are raising to
# Space complexity: O(1) since no extra storage is used

def divisionPow(a, b):
	if b < 0.0:
		return None

	if b == 0.0:
		return 1.0
	elif b == 1.0:
		return a

	if b % 2 == 0:	# O(log b) where b is the power you are raising to
		square = divisionPow(a, b/2)
		return square * square
	elif b % 2 == 1:
		return divisionPow(a, b/2 + 1) * divisionPow(a, b/2)

print(divisionPow(2, 20))

memo = {0: 1}
def memoizedDivisionPow(a, b, memo):
	if b < 0.0:
		return None

	if 1 not in memo:
		memo[1] = a
		
	if b in memo:
		return memo[b]
	else:
		if b % 2 == 0:
			square = memoizedDivisionPow(a, b/2, memo)
			memo[b] = square * square
		elif b % 2 == 1:
			memo[b] = memoizedDivisionPow(a, b/2 + 1, memo) * memoizedDivisionPow(a, b/2, memo)

		print memo

	return memo[b]

print(memoizedDivisionPow(2, 20, memo))