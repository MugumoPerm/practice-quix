#create a function two_sum
#@param numbers, target
#The function returns the index of the number of which the sum equals to the target

def two_sum(numbers, target):
    ln = len(numbers)

    for i in range(ln):
        for j in range(ln):
            if numbers[i]+numbers[j] == target:
                if i != j:
                    return ([i, j])
    
    
print(two_sum((2,2,3), 4))