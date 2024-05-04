class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        temp=[]
        if s==" " or len(s)==1:
            length=1
        else:
            for i in range(len(s)):
                temp.append(s[i])
                for j in range(i+1,len(s)):
                    if(s[j] not in temp):
                        temp.append(s[j])  
                        if(j==len(s)-1):
                            length=max(len(temp),length)  
                            temp.clear()
                    else:
                        length=max(len(temp),length)
                        temp.clear()
                        break
                    

        return length
