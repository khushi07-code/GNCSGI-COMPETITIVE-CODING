class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer=''
        j=0
        for i in range(len(s)):
            if j<len(spaces) and i == spaces[j]:
                answer=answer+" "+s[i]
                j+=1
              
            else:
                answer+=s[i]
        return answer        

