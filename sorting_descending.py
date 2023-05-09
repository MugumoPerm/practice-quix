def desc(num):
    digits = str(num)
    ln = len(digits)
    a = []
    sorted = []
    for i in range(0, ln):
        a.append(digits[i])
    
    pivot = a[3]
    for i in range(ln):
        for j in range(ln):
           #print(a[j], a[i]) 
           if a[i]>a[j]:
               a.pop(j)
               print(a[i])
    
    
    
    
print(desc(1238396))