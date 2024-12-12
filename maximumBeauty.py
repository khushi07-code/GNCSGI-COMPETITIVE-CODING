# Example 1:

# Input: nums = [4,6,1,2], k = 2
# Output: 3
# Explanation: In this example, we apply the following operations:
# - Choose index 1, replace it with 4 (from range [4,8]), nums = [4,4,1,2].
# - Choose index 3, replace it with 4 (from range [0,4]), nums = [4,4,1,4].
# After the applied operations, the beauty of the array nums is 3 (subsequence consisting of indices 0, 1, and 3).
# It can be proven that 3 is the maximum possible length we can achieve.
# Example 2:

# Input: nums = [1,1,1,1], k = 10
# Output: 4
# Explanation: In this example we don't have to apply any operations.
# The beauty of the array nums is 4 (whole array).
# 


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        maxlen=0
        j=0
        for i in range(n):
                while j<n and  nums[j]-nums[i]<=2*k:
                    j+=1
                maxlen=max(maxlen,j-i)
        return maxlen        
