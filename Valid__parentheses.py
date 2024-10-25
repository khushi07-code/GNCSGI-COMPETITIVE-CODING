# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        valid=False
        for i in s:
            if i=="(" or i== "[" or i=="{":
                l.append(i)
            else:
                if not l: 
                    return False
                opposite=l.pop()
                if (opposite == "(" and i == ")") or (opposite == "[" and i == "]") or (opposite == "{" and i == "}"):
                    valid=True
                else:
                    return False
        if  l:
            return False
        return valid
