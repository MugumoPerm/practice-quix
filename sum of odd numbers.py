# Calculate the sum of the numbers in the nth row of this triangle 
# (starting at index 1) e.g.: (Input --> Output)

def row_sum_odd_numbers(n):
    
    #create the odd numbers
    num = []
    for i in range(0,3*3):
        if i%2 == 1:
            
            num.append(i)
            
    print(num)
            
            
print(row_sum_odd_numbers(5))