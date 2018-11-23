# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Given two positive integers p and q, return an p x q grid with a
clockwise spiral of the numbers from 1 to p*q ascending starting from the
top left corner.
 
Example Input:
p=3, q=4
 
Example Output:
[
    [1,  2,  3,  4],
    [10, 11, 12, 5],
    [9,  8,  7,  6],
]
"""
def changeDirection(direction, matrix, col, row, p, q):
    if direction == "right" and (col == q - 1 or matrix[row][col + 1] != 0):
        direction = "down"
    elif direction == "down" and (row == p - 1 or matrix[row + 1][col] != 0):
        direction = "left"
    elif direction == "left" and (col == 0 or matrix[row][col - 1] != 0):
        direction = "up"
    elif direction == "up" and (row == 0 or matrix[row - 1][col] != 0):
        direction = "right"
        
    return direction

def spiralMatrix(p, q):
    matrix = []
    
    # Create spiral matrix and initialize all p x q values to 0
    for i in range(0, p):
        newList = []
        
        for j in range(0, q):
            newList.append(0)
            
        matrix.append(newList)
        
    value = 1
    upperBound = p * q
    
    direction = "right"
    row, col = 0, 0
    while value <= upperBound:
        matrix[row][col] = value
        
        if direction == "right":
            col += 1
        elif direction == "down":
            row += 1
        elif direction == "left":
            col -= 1
        else:
            row -= 1
            
        direction = changeDirection(direction, matrix, col, row, p, q)
            
        value += 1
    
    for lst in matrix:
        print(lst)
        print("\n")
    
    return
    
#  spiralMatrix(3, 4)
spiralMatrix(10, 10)