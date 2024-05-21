class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, n = [], len(nums)
        for i in range(1 << n):
            s = []
            for j in range(n):
                if i >> j & 1:
                    s.append(nums[j])
            ans.append(s)
        return ans
