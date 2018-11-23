
"()()()()" -> true
")(()" -> false

')' -> false

def matched(string):
    if string == "":
        return True

    stack = []
    matchDict = {'(': ')', '{', '}', '[', ']'}

    for char in string:
        if char in matchDict:
            stack.append(char)
        elif not stack:
            return False
        elif char == matchDict[stack[-1]]:
            stack.pop(-1)

    if not stack:
        return True
    return False
        
input: ["the", "quick", "brown", "fox", "quick"]
distance("fox", "the") = 3
distance("quick", "fox") = 1

# wordDict = {"fox": [3], "the": [0]}


func distance(w1: String, w2: String) -> Int

distance(["the", "quick", "brown", "fox", "quick"], "quick", "fox")

wordDict = {"quick": [1, 4], "fox": [3]}
distances = [2, 1]
abs(1 - 3) = 2
abs(4 - 3) = 1

# class DistanceFinder:
#     self.wordDict = {}

#     def distance(self, lst, w1, w2):
#         if w1 not in wordDict:
#             self.wordDict[w1] = []
#         if w2 not in wordDict:
#             self.wordDict[w2] = []

def distance(lst, w1, w2):
    wordDict = {w1: [], w2: []} 

    # O(n)
    for i in range(0, len(lst)):
        if w1 == lst[i]:
            wordDict[w1].append(i)
        elif w2 == lst[i]:
            wordDict[w2].append(i)

    # Append all the differences to the distances list
    # O(m * n)
    minimum = sys.maxint
    for i in range(0, len(wordDict[w1])):
        for j in range(0, len(wordDict[w2])):
            if (abs(wordDict[w1][i] - wordDict[w2][j])) < minimum:
                minimum = (abs(wordDict[w1][i] - wordDict[w2][j]))
            
    # Return minimum value in distances
    # O(n)
    return minimum




    
    
