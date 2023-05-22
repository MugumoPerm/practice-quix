# this is a solved case of the three sum problem
# @param nums

#import the listing function
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        list = []
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if i != j and i != k and j != k :
                            list.append(([nums[i],nums[j],nums[k]]))
        return(list)
                    
                    
threesum = Solution()

print(threesum.threeSum(nums=[-1,0,1,2,-1,-4]))

