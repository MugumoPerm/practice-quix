from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(length):
            for j in range(length):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return [i, j]
        else: return None
        



nums = [1,1,2,3,4]
twosum = Solution()
print(twosum.twoSum(nums,target=2))