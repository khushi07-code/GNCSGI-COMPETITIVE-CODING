 # [1,n]
# Example 1:
# Input: banned = [1,6,5], n = 5, maxSum = 6
# Output: 2
# Explanation: You can choose the integers 2 and 4.
# 2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set=set(banned)
        num_sum=0
        count=0
        for i in range(1,n+1):
            if i not in banned_set and (num_sum+i)<=maxSum:
                num_sum+=i
                count+=1
        return count
