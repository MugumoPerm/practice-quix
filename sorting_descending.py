def sorting(num):
    arr = num
    if len(arr)< 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
        return sorting(greater) + [pivot] + sorting(lesser)
    


print(sorting([1,2,1,3]))

