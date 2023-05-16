# find the transition index where the sum of left integers are equal to the sum of the right integers
#return -1 if there is no transtional index
#else return the transition index
#@param arr

def find_even_index(arr):
    ln = len(arr)
    count = 0
    index = 0
    
    if sum(arr[1:]) == 0:
            return 0
    
    for i in range(ln):
        
        pivot = arr[i]
    
        # print (pivot)
        left = arr[:i]
        right = arr[arr.index(pivot):]
        
        print (left,pivot,right[1:])
        index += 1
        
        
        if sum(left) == sum(right[1:]):
            count += 1
        else:
            return -1
    if count == 1:
        return index-1
    
    else:
        return -1
    
        


print(find_even_index([10, 4, 13, -20, -18, -14, 4, 14, 4, 10, -18, -9, 15, -20, -14, 13, -20]))