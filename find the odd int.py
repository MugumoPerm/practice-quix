# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

#create a function find_it 

def find_it(seq):
    #find the length of the array
    ln = len(seq)
    number_count = []
    #create a loop to find the count of each element in the array
    for i in range(ln):
        #get the count of the array
        count = seq.count(seq[i])
        #find the modulus of 2 to the count to get the odd number
        if count % 2 == 1:
            odd = seq[i]
            
            #append all the odd numbers to get the length of appended array
            number_count.append(seq[i])
    #if the length of the appended is greater than zero return the odd number 
    if   len(number_count) > 0:
        
        return odd
    #else return none
    else:
        return None
    


    


print(find_it([1,1,1,1,1,2,2,2,1,1,1,5,5,5,1,1]))