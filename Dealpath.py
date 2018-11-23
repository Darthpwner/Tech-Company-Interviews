
# Print out "A,BC,DEFG,HI" with the commas

#
#      A
#     / \
#    B   C
#   /|\  |
#  D E F G
#    |   |
#    H   I
#  
#

# top level loop: used to determine when to stop looping
# 2nd level loop: used to loop through a level
# 3rd level loop: used to loop through children from nodes on that level and queue up what's in the next level

def traverseTree(node):
    queue = [node]
    # level = [node]
    currentLevel = [node]
    nextLevel = []
    
    while queue:
        if not currentLevel:
            for i in nextLevel:
                print("nextLevel: {}".format(i.data))
            currentLevel = nextLevel
            nextLevel = []
        
        for node in currentLevel:
            print node.data    # print current level
            
            for child in currentLevel:    # populate next level
                queue.append(child)
                nextLevel.append(child)      
                
            del queue[0]
            del currentLevel[0]
              

class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children


i = Node("I", []);
h = Node("H", []);
g = Node("G", [i]);
f = Node("F", []);
e = Node("E", [h]);
d = Node("D", []);
c = Node("C", [g]);
b = Node("B", [d,e,f]);
a = Node("A", [b,c]);

traverseTree(a);