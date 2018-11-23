
def hasContinuousSum(lst, sum):
	total = 0
	memo = {}
	
	for i in range(0, len(lst)):
		total += lst[i]

		if total not in memo:
			memo[total] = True

		if total - sum in memo:
			return True

	return False

print(hasContinuousSum([1, 6, 3], 9))
print(hasContinuousSum([1, 6, 4], 9))

# LRU Cache (Slow)
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.i = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:   # Key not found in cache
            return -1
        
        self.i += 1
        self.cache[key] = (self.cache[key][0], self.i)
        return self.cache[key][0]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if key not in self.cache and len(self.cache) >= self.capacity:    # Remove least recently used item if key is NOT in cache
            minValue = sys.maxint
            for i in self.cache:
                if self.cache[i][1] < minValue:
                    minValue = self.cache[i][1]
                    lru = i
                                
            self.cache.pop(lru)
        self.i = self.i + 1
        self.cache[key] = (value, self.i)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)