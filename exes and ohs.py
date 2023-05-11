# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. 
# The string can contain any char.

#create a function to return true or false
def xo(s):
    #identify the xo in the x and o varaiables
    x = 'xX'
    o = 'oO'
    #get the length of s
    ln = len(s)
    
    #declare a count variable of x and y
    countx = 0
    counto = 0
    
    #check whether s has any of the x or o
    for i in range(ln):
        if s[i]  in x:
            countx +=1
        elif s[i]  in o:
            counto +=1 
    #if count of o equals the count of x then the condition is met
    if counto == countx:
        return True
    #if a false is printed
    else:
        return False
    
    
print(xo('Xoxoxoxoxoxoxo'))