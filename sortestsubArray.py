class Solution: 
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int: 
        n=len(arr) 
        length=0 
        mid=(0+n-1)//2 
        prestack=[] 
        for i in arr: 
            if prestack and prestack[-1]>i:
                break 
            prestack.append(i) 
        sufstack=[] 
        for i in arr[::-1]: 
            if sufstack and sufstack[0]<i: 
                break 
            sufstack.insert(0,i) 
        if prestack==sufstack: 
            return 0 
        for i in range(len(prestack)-1,-1,-1): 
            stack=[] 
            for j in range(len(sufstack)): 
                if prestack[i]<=sufstack[j]: 
                    stack=prestack[:i+1]+sufstack[j:] 
                    length=max(length,len(stack)) 
        length=max(length,len(sufstack)) 
        length=max(length,len(prestack)) 
        return len(arr)-length
