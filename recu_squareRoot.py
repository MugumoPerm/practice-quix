def refine(a, b):
    if b * b == a:
        return b
    elif b * b < a:
        return -1
    
    else:
       return refine(a, b-1)
        
        
        
def sqrt(a):
    b = int(a//2)
    
    if a == 1:
        return 1
    else:
        return refine(a, b)
        
        
        
        
print(sqrt(144))