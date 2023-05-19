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
                

nums = [1,2,4,5]
large = Solution()

print(large.containsDuplicate(nums))