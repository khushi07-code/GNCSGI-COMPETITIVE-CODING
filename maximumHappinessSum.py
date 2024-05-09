class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        s=happiness[0:k]
        nve=0
        m=k-1
        for i in range(len(s)-1,0,-1):
            if(s[i]-m>=0):
                   break
            nve+=(s[i]-m)
            m-=1   
        num=0
        for i in range(k-1,0,-1):
            num+=i
        return sum(s)-(num+nve)
        
  
        
