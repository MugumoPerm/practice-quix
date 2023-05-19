#problem: rearrange the list or array to get the largest number
#@param nums
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        num_count = []
        for i in range(length):
            present_twice = nums.count(nums[i])
            num_count.append(present_twice)
        if 2 in num_count:
            return True
        else:
            return False

    
        
        
        
nums = ([1,2,3,4,5])        
large = Solution()

print(large.containsDuplicate(nums))