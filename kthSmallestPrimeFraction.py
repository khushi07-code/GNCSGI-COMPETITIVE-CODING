class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def div(s):
            return s[0]/s[1]
        temp=[]
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if(arr[i]!=arr[j]):
                    temp.append([arr[i],arr[j]])
        temp=sorted(temp,key=div)
        return temp[k-1]

