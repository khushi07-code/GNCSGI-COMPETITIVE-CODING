# You are given a 0-indexed binary string s having an even length.

# A string is beautiful if it's possible to partition it into one or more substrings such that:

# Each substring has an even length.
# Each substring contains only 1's or only 0's.
# You can change any character in s to 0 or 1.

# Return the minimum number of changes required to make the string s beautiful.

class Solution:
    def minChanges(self, s: str) -> int:
        change=0
        i=0
        while i<len(s):
            if s[i]!=s[i+1]:
                change+=1
            i+=2
        return change
