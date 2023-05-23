def twoSum(nums, target):
    left = 0  # Pointer starting from the left end of the array
    right = len(nums) - 1  # Pointer starting from the right end of the array
    nums = sorted(nums)
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]  # Found the pair, return the indices
        elif curr_sum < target:
            left += 1  # Move the left pointer to the right
        else:
            right -= 1  # Move the right pointer to the left

    return None  # No valid pair found

# Example usage
nums = [15, 4, 7, 11, 2]
target = 9
result = twoSum(nums, target)
if result:
    print(f"The pair of indices that sum up to {target} is: {result}")
else:
    print("No valid pair found.")
