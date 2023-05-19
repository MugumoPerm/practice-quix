#problem: rearrange the list or array to get the largest number
#@param nums
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        num_count = 0
        atleast_twice = 2
        for i in range(length):
            present_twice = nums.count(nums[i])
            if present_twice >= 2:
                num_count += 1
        if num_count >0:
            return True
        else:
            return False
                
    
        
        
        
nums = ([7,10,5,5,6,6,4,10,5,4,9,4,9,6,5,9,6,3,6,5,6,7,7,4,9,9,10,5,8,1,8,3,2,7,5,10,1,8,5,8,4,3,6,4,9,4,2,8,3,2,2,1,5,6,3,2,6,1,8,6,2,9,1,4,5,10,8,5,10,5,10,1,4,8,3,6,4,10,9,1,1,1,2,2,9,6,6,8,1,9,2,5,5,2,1,8,5,2,3,10])        
large = Solution()

print(large.containsDuplicate(nums))