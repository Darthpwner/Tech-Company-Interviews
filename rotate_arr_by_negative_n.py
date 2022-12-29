n = 2
  
list_1 = [10, 20, 30, 40, 50, 60] 
print("List:", list_1)
list_1 = (list_1[-n:] + list_1[:-n]) 
print("Rotated list:",list_1)