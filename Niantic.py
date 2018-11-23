
class Person:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.friends = {'B', 'D'}
    
    self.possiblePaths = []
    
 person 'A'
self.friends = 'B'


A -> E

A -> {B}
B -> {A, D, C}
C -> {B, E}
D -> {B}
E -> {C}

possiblePaths = [[A, B, C, E]]
path = [A, B, C, E]

encountered = {}

  def getPaths(self, start, end, path):
      if start == end:
          self.possiblePaths.append(path)
          return path
      
      while friend in self.friends:
          if friend not in self.encountered:
            self.encountered[friend] = True
        
          if friend in self.encountered:
              continue 
        
          path.append(node)
          self.getPaths(node, end, path)
          
      return

  def shortestPath(self, start, end):
      path = [start]
      self.getPaths(start, end, path)
#       Call getPaths on all possible paths
#       self.possbilePaths has all possible paths
#       return min of all inner lists
        
#       start: [potential nodes to go]

A-B-C-E
  |   |
  D - F

