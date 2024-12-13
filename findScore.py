# Find Score of an Array After Marking All Elements


# Input: nums = [2,1,3,4,5,2]
# Output: 7
# Explanation: We mark the elements as follows:
# - 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
# - 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
# - 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
# Our score is 1 + 2 + 4 = 7.


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score=0
        n=len(nums)
        mark=[False]*n
        temp=[(num,idx)for idx,num in enumerate(nums)]
        temp.sort()
        for i in range(n):
            number=temp[i][0]
            index=temp[i][1]
            if not mark[index]:
                score+=number
                mark[index]=True
                if index-1>=0:
                   mark[index-1]=True
                if index+1<n:
                    mark[index+1]=True
        return score            
                   
                
            
      
