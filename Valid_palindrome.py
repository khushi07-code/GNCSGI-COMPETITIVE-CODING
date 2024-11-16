# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.



class Solution:
    def isPalindrome(self, s: str):
        ans=''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric() :
                if s[i].isupper():
                    ans+=s[i].lower()
                else:
                    ans+=s[i]

        print(ans)
        if ans==ans[::-1]:
            return True
        return False
                  






        
        
