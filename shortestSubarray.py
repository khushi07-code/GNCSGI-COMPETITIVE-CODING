# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.


from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        print(prefixSum)
        
        length = float('inf')
        dq = deque()
        print(dq)
        for i in range(n + 1):
            while dq and prefixSum[i] - prefixSum[dq[0]] >= k:
                print(dq[0])
                print( prefixSum[i] - prefixSum[dq[0]])
                length = min(length, i - dq.popleft())
            
            while dq and prefixSum[i] <= prefixSum[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return length if length != float('inf') else -1


