import string
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        letters = string.ascii_letters
        i=0
        j=0
        while i<len(str1) and j<len(str2):
            if str1[i]==str2[j] or letters[letters.index(str1[i])+1].lower()==str2[j]:
                i+=1
                j+=1
            else:
                i+=1
        print(j)
        if j==len(str2):
            return True
        else:
            return False
        
