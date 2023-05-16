# find the transition index where the sum of left integers are equal to the sum of the right integers
#return -1 if there is no transtional index
#else return the transition index
#@param arr

def find_even_index(arr):
    ln = len(arr)
    if sum(arr) == 0:
        return 0
    if sum(arr[:]) == sum(arr[1:]):
        return -1
    add = 0
    for i in range(ln):
        n = ln -i
        for j in range(-1,ln):
            
            # if len(arr[j:]) and len(arr[:i])==int(ln/2):
            if arr[j:] != arr[:i]:
                if sum(arr[j:]) == sum(arr[:i]):
                    if (len(arr[j:]))  >= int(ln/2) or (len(arr[:i])) >= int(ln/2):
                        
                        list1 = (arr[j:])
                        list2 = (arr[:i])
                        print(list1)
                        print(list2)
                        print(sum(list1),sum(list2))
                        list2.extend(list1)
                        if arr[:i] == []:
                            return 0
                        else:
                            if ln%2 == 0:
                                return -1
                        
                            for i in range(ln):
                                add +=1
                                if list2[i] != arr[i]:
                                    
                                    if arr.count(arr[i]) == 1:
                                        return add-1
                                    
                                    else:
                                        return (add-2)
    else:
        return -1
                    
     
    
    
    
print(find_even_index([10,-80,10,10,15,35,20]))