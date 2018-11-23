class Solution(object):
    def changeDirection(self, direction, matrix, r, c, rows, cols):
        if direction == "right" and (c == cols - 1 or matrix[r][c + 1] == -1):
                direction = "down"
            elif direction == "down" and (r == rows - 1 or matrix[r + 1][c] == -1):
                direction = "left"
            elif direction == "left" and (c == 0 or matrix[r][c - 1] == -1):
                direction = "up"
            elif direction == "up" and (r == 0 or matrix[r - 1][c] == -1):
                direction = "right"
                
        return direction
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        length = rows * cols
        
        i = 0
        r, c = 0, 0
        direction = "right"
        while i < length:
            spiral.append(matrix[r][c])
            
            matrix[r][c] = -1   # Mark traversal
            
            if direction == "right":
                c += 1
            elif direction == "down":
                r += 1
            elif direction == "left":
                c -= 1
            elif direction == "up":
                r -= 1
                
            direction = self.changeDirection(direction, matrix, r, c, rows, cols)
                
            i += 1
            
        return spiral