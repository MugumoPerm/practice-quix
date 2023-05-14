# Calculate the sum of the numbers in the nth row of this triangle 
# (starting at index 1) e.g.: (Input --> Output)

def row_sum_odd_numbers(n):
    
    #create the odd numbers
    num = []
    row = []
    for i in range(1,40):
        if i%2 == 1:
            # print(i)
            num.append(i)
    print (num)
    for i in range(0,len(num)):
        print(num[i+2])
print(row_sum_odd_numbers(4))