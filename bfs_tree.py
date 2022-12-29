class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.value = key

def printLevelOrder(root):
	# Base case
	if root is None:
		return

	# Create an empty queue for level order traversal
	queue = []

	# Enqueue the root and initialize height
	queue.append(root)

	while len(queue) > 0:
		print(queue[0].value)
		node = queue.pop(0)

		# Enqueue left child
		if node.left is not None:
			queue.append(node.left)

		# Enqueue right child
		if node.right is not None:
			queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)