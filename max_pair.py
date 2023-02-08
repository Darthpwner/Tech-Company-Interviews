# please write a function that will output the indices of the two consecutive elements that have the highest max sum in an input array of integers 
# (e.g., maxPair([0, 5, 5, 2]) will return (1, 2)). In the case of a tie, the method should return the leftmost pair 
# (e.g., maxPair([0, 4, 3, 1, 2, 3, 4, 0]) will return (1, 2)).

def maxPair(list):
	i, j = 0, 1

	maxSum = 0
	indices = None
	while j < len(list):
		currSum = list[i] + list[j]
		if currSum > maxSum:
			maxSum = currSum
			indices = (i, j)
		i += 1
		j += 1
	return indices

print(maxPair([0, 5, 5, 2]))				# (1, 2)
print(maxPair([0, 4, 3, 1, 2, 3, 4, 0]))	# (1, 2)
print(maxPair([0, 4]))	# (0, 1)
print(maxPair([0]))	# None
print(maxPair([]))	# None