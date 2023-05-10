# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

#create a function find_it 

def find_it(seq):
    #find the length of the array
    ln = len(seq)
    
    #create a loop to find the count of each element in the array
  
    for i in range(ln):
        count = seq.count(seq[i])
        
        if count%2 != 0 :
            print(seq[i])
    
    
    
    return None



find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])