Class Node:
	Def __init__(self, value):
		Self.value = value
		Self.next = None
		Self.prev = None

class LRUCache:
	def __init__(self, capacity):
		Self.capacity = capacity
		Self.cache = {}	# key: <linked list>
		Self.priority = 0

		Self.front = Node(0)
		Self.back = Node(0)

		Self.front.next = self.back
                       Self.back.prev = self.front
		Self.back.next = None

	Def get(self, key):
		if key not in self.cache:
			Return -1
                       Node = self.cache[key]
		self.remove(Node)	# Delete LRU version
		self.insert(Node)	# Update to be most recently used

		Return Node.value

	Def put(self, key, value):
		If key not in self.cache:
			Self.cache[key] = Node(value)
		Node = self.cache[key]

		If len(self.cache) > self.capacity:
			self.remove(self.back.prev)	# Delete LRU version				
self.insert(Node)	# Insert MRU key, value at the front

	Def insert(self, node):
		newNode = Node(value)

		newNode.prev = self.front
		newNode.next = self.front.next
		
		Self.front.next.prev = newNode
		Self.front.next = newNode
		
	Def remove(self, node):
		Node.prev.next = node.next
		Node.next.prev = node.prev

		Node.next = None
		Node.prev = None

