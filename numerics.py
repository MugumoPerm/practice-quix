#create a function that takes in a positive number and prints out the roman numbers
# TODO convert int to roman string

def solution(n):
    
   
    mod = n%10
    
    dm = (divmod(n,9))
    print(dm)
    print(dm[0])
    print(mod)



print(solution(8000))
   
   
   
   
    