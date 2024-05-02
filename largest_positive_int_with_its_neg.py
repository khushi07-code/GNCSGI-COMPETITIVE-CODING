# Largest positive integer that  exits with its negative

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        answer=0
        for i in nums:
            if(i>0):
                if nums.count(-i):
                    if(answer<i):
                        answer=i
        if(answer==0):
            answer=-1
        return answer



        
