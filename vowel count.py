# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

#create a function to solve the problem
def get_count(sentence):
    #find the length of the sentence
    ln = len(sentence)
    #define the vowels
    vowels = "aeiou"
    #if the sentence or string is empty return 0
    if ln <= 0:
        return 0
    #count the number of vowels in the sentence
    else:
        count = 0
    #loop through the sentence checking each element is the sentence
        for i in range(ln):
            #give a conditional statement to get only the vowels
            if sentence[i] in vowels:
                #this is the counter of the vowels found
                count += 1
        #return the number count of the vowels found
        return (count)



print(get_count(''))