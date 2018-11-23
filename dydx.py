''''
:type magic_number: int 
:type numbers: list[int]
:type rtype: bool
'''
def arithmetic_boggle(magic_number, numbers):
    # Brute Force
    if not numbers and magic_number == 0:
        return True
    elif not numbers:
        return False

    sum = numbers[0]    
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            for z in range(j, len(numbers)):
                sum += numbers[z]
                print("numbers: {}".format(numbers))
                print("sum: {}".format(sum))
        
            if sum == magic_number:
                return True
            sum = numbers[0]
            numbers[j] *= -1
        numbers[i] *= -1
    
    
    if sum == magic_number:
        return True
    return False
    
    

arithmetic_boggle(2, [1, 2, 3, 4])