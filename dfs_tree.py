class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def print_inorder_traversal(root):
	if root:
		print_inorder_traversal(root.left)
		print(root.val)
		print_inorder_traversal(root.right)

def print_preorder_traversal(root):
	if root:
		print(root.val)
		print_preorder_traversal(root.left)
		print_preorder_traversal(root.right)

def print_postorder_traversal(root):
	if root:
		print_postorder_traversal(root.left)
		print_postorder_traversal(root.right)
		print(root.val)

root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

   #     1
   #    / \
   #   2   3
   #  / \
   # 4   5
 
print("Inorder traversal:")
print_inorder_traversal(root)
print("Preorder traversal:")
print_preorder_traversal(root)
print("Postorder traversal:")
print_postorder_traversal(root)