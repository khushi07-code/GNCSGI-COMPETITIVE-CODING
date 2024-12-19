# Example 2:

# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count=0
        k=0
        n=len(arr)
        while k<n:
            start=k
            while 1:
                Ar=[i for i in range(start,k+1)]
                c=0
                for i in arr[start:k+1]:
                    if i in Ar:
                        c+=1
                if c==(k+1-start):
                    count+=1
                    k+=1
                    break
                else:
                    k+=1
        return count  

            
            


 
           


        
