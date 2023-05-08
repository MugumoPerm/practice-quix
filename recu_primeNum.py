def iterator(a, b):
    if a % b == 0:
        return False
    elif (b * b) > a:
        return True
    else:
        return iterator(a, b+1)
    
    
    
def check_prime(a):
    b = 2
    if a < 2:
        return False
    else:
        return iterator(a, b)
    
    
print(check_prime(6))