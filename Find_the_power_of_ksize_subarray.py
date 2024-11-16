# You are given an array of integers nums of length n and a positive integer k.

# The power of an array is defined as:

# Its maximum element if all of its elements are consecutive and sorted in ascending order.
# -1 otherwise.
# You need to find the power of all 
# subarrays
#  of nums of size k.

# Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result=[]
        left=0
        right=k
        while right<=len(nums):
            if all(nums[i]+1==nums[i+1] for i in range(left,right-1)):
                result.append(max(nums[left:right]))
            else:
                result.append(-1)
            left+=1
            right+=1
        return result
