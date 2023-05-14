# function to return the sum of the nth term
#@param n(nth term)

def series_sum(n):
    fraction = []
    add = []
    for i in range(4,n*7,3):
        fraction.append(1/i)
    fraction.insert(0, 1)
    
    for i in range(0, n):
        add.append(fraction[i])
    summation = (sum(add))
    formatted_number = f"{summation:.2f}"
    return formatted_number
        
print(series_sum(9))