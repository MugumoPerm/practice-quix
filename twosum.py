from typing import List
class Solution:
    def twoSum(self,nums, target):
        left = 0  # Pointer starting from the left end of the array
        right = len(nums) - 1  # Pointer starting from the right end of the array
        nums = sorted(nums)
        
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                return ([nums[left], nums[right]]), ([left, right]) # Found the pair, return the indices
            elif curr_sum < target:
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left

        return None  # No valid pair found


        



nums = [4,1,2,23,4,5,4,675,7,4,3,2,2,3,4,6,75,7,3,1]
twosum = Solution()
print(twosum.twoSum(nums,target=40))