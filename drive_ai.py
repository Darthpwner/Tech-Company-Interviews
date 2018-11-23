def reverseLL(node):
	prev = None
	curr = node
	
	while curr:
		nextPtr = curr.next
		curr.next = prev

		prev = curr
		curr = nextPtr

	return prev