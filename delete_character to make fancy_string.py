# A fancy string is a string where no three consecutive characters are equal.

class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=""
        for i in range(len(s)):
            if i==0:
                ans+=s[0]
            elif i==1:
                ans+=s[1]
            elif s[i]!=s[i-1] or s[i]!=s[i-2]:
                ans+=s[i]
        return ans
