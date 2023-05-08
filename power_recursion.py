def powr(x, y):
    if y == 0:
        return 1
    
    else:
        
        return x * powr(x, y-1)
    
    
    
print(powr(2, 4))