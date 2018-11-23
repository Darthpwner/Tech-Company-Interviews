def integerCount(n1, n2):
    count = 0
    
    power = 0
    tmp = n2
    while tmp > 0:
        tmp /= 10
        power += 1

    print("power: {}".format(power))
    while n1 > 0:
        digit = n1 % (10 ** power)
        if n2 == digit:
            count += 1
        
        n1 /= 10
    
#     n1String = str(n1)
#     n2String = str(n2)
    
#     for char in n1String:
#         if char == n2String:
#             count += 1
            
    return count
    
    #function ( int , int ) -> int
    #    ( 1231123 , 1 ) -> 3
    
print(integerCount(1231123, 1))    # 3
print(integerCount(10231123, 10))    # 3


#