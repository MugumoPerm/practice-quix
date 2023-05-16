# find the transition index where the sum of left integers are equal to the sum of the right integers
#return -1 if there is no transtional index
#else return the transition index
#@param arr

def find_even_index(arr):
    ln = len(arr)
    count = 0
    for i in range(ln):
        
        pivot = arr[i]
    
        # print (pivot)
        left = arr[:i]
        right = arr[arr.index(pivot):]
        
        # print (left,pivot,right[1:])
        
        if sum(left) == sum(right[1:]):
            count += 1
            index = pivot
            break
    if count == 1:
        return index
    
    else:
        return -1
    
        


print(find_even_index([10,20,30,30,20,10]))