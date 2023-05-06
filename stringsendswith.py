#Complete the solution so that it returns true if the first argument(string) passsed in ends with the 2nd argument (also a string). 

#create a function to check if the string ends with the words
#two parameters are defined: name and the string

def solution():
    
    #define the variable name
    name = 'fail'
    word = 'al'

    # get the length
    ln = len(name)
    lnw = len(word)

    #check if the last letter of the name is equal to the last letter of the word
    if name[ln-1] != word[lnw-1]:
        return False
    
    #if true continue 
    else:
        #initialize the looping variable
        i = lnw
        
        #loop the name and word to check whether they are the same
        while(i>=1 and ln>=1):
            
            #check if they are the same
            if name[ln-1] not in word[i-1]:
                return False
            
            #decrement the string
            i = i-1
            ln -= 1
        #rerurn true if the conditions are met
        return True
                    
print(solution())