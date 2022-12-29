n=1	# The number of shifts we want to do
  
list_1 = [11, 22, 33, 44, 55] 
print("List:", list_1)
list_1 = (list_1[len(list_1) - n:len(list_1)]  
                 + list_1[0:len(list_1) - n]) 
print("Rotated list:", list_1)