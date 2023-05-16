# # find the transition index where the sum of left integers are equal to the sum of the right integers
# #return -1 if there is no transtional index
# #else return the transition index
# #@param arr

# def find_even_index(arr):
#     length = len(arr)
    
#     for i in range(length):
#         sum = 0
#         for j in range(i):
#             sum += arr[j]
        
#         sum2 = 0
#         for j in range(i+1,length):
#             sum2 += arr[j]
            
#         if sum == sum2:
#             return i   
#     else:
#         return -1     
        
# print(find_even_index([-12, 23, 7, -32, 10, 11, 4, 4, 13, 11, 10, 13, 4, 4, -10, -12]))


#alternative code 

def find_even_index(arr):
    length = len(arr)
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(length):
        total_sum -= arr[i]
        
        if left_sum == total_sum:
            return i
        
        left_sum += arr[i]
    
    return -1


print(find_even_index([1,2,3,4,3,2,1]))


