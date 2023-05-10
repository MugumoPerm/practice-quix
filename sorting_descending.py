def sorting(num):
    arr = num
    if len(arr)< 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
        return sorting(lesser) + [pivot] + sorting(greater)
    


print(sorting([9,2,3,4,5,7,8,9,6]))

