# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # Two cases:
    # (1) n_th item included
    # (2) not included
    included = val[n - 1] + knapSack(W - wt[n - 1], wt, val, n -1)
    excluded = knapSack(W, wt, val, n - 1)

    # If weight of n_th item is > Knapsack of capacity W, we cannot include this item in the optimal solution
    if wt[n - 1] > W:
        return excluded

    # Return the max of these two cases:
    
    else:
        return max(included, excluded)
  
# To test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print knapSack(W , wt , val , n) 

# DP version of knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W 
def dpKnapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]   # Build out your table K

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][w]
 
# Driver program to test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(dpKnapSack(W, wt, val, n)) 
  
# This code is contributed by Bhavya Jain 
