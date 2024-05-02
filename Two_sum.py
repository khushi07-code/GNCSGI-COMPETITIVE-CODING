# return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    answer.append(i)
                    answer.append(j)
        return answer
    


        
