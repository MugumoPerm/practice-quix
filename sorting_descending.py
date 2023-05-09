def desc(num):
    digits = str(num)
    ln = len(digits)
    a = []
    sorted = []
    for i in range(0, ln):
        a.append(digits[i])
    
    return a

def sorting(num):
    arr = desc(num)
    if len(arr)<= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        
        return sorting(greater) + [pivot] + sorting(lesser)
    


print(sorting(1213))

