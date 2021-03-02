class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def delete_node_with_given_key(head, key):
	node = head
	if head.val == key:
		node = head.next
		head.next = None
		print("Deleted key: {}".format(key))
		return node

	while node.next:
		print("node.val: {}".format(node.val))
		if node.next.val == key:
			node.next = node.next.next
			print("Deleted key: {}".format(key))
			return head
		node = node.next

	print("Unable to find key. Linked list unchanged.")
	return head

def print_lst(head):
	while head:
		print(head.val)
		head = head.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

print_lst(n1)
delete_node_with_given_key(n1, 1)
print_lst(n2)
delete_node_with_given_key(n2, 5)
print_lst(n2)
