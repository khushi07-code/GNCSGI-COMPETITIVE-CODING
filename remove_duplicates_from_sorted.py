class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        i=0
        while i<len(nums):
            if nums[i]=="_":
                return k
            c=nums.count(nums[i])
            k=k+1
            if c!=1:
                for j in range(1,c):
                    nums.remove(nums[i])
                    nums.append("_")
            i=i+1
