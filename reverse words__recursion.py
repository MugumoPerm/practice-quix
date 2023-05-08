# f = 1

# def factorial(n):
    
#     if n == 1:
#         return 1
    
#     else:
#         return n * factorial(n+1)
    
    
# print(factorial(5))


name = 'perminus karanja'


def rec(name, index=0):
    ln = len(name)
    
    if index == ln:
        return
    
    rec(name, index+1)
    print(name[index])

rec(name)













