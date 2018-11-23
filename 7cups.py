
# 1. Fizz Buzz
# Write a function f(n), such that it returns:
# "Zif" if n is evenly divisable by 3
# "Zub" if n is evenly divisable by 4
# "Zif Zub" n is evenly divisable by 12
# Otherwise, n

# Evaluate f(n) over a range of integer values from 1 to 100

def fizzBuzz(n):
	if n % 12 == 0:
		return "Zif Zub"
	elif n % 3 == 0:
		return "Zif"
	elif n % 4 == 0:
		return "Zub"
	else:
		return n

for i in range(1, 100):
	print(fizzBuzz(i))
print("\n")

# 2. Fibonacci 
# Write a function f(n), such that for any positive integer value of n, it returns the integer at the nth position in the series below:
# 1,1,2,3,5,8,13...

memo = {0: 1, 1: 1}

def fibonacci(n, memo):
	if n not in memo:
		memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

	return memo[n]


for i in range(0, 10):
	print(fibonacci(i, memo))
print("\n")

# 3. Anagram
# Write a function f(n, m), such that n and m are strings and it returns:
# true if m is an anagram of n
# false if m is not an anagram of n
# Anagram: a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

def anagram(n, m):
	dict = {}

	for char in n:
		if char not in dict:
			dict[char] = 1
		else:
			dict[char] += 1

	for char in m:
		if char in dict:
			if dict[char] == 0:
				del dict[char]
			dict[char] -= 1
		else:
			return False

	return True

print(anagram("cinema", "iceman"))
print(anagram("cinema", "icemanz"))
print("\n")
	
# Bubblesort
def bubblesort(n):
	noSwaps = True

	for i in range(0, len(n)):
		for j in range(0, len(n) - 1):
			if n[j + 1] < n[j]:
				temp = n[j + 1]
				n[j + 1] = n[j]
				n[j] = temp
				noSwaps = False

		if noSwaps:
			break

	return n

print(bubblesort([5, 1, 4, 2, 8]))
print("\n")

