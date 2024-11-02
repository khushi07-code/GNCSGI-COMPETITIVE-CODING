# A sentence is circular if:
# The last character of a word is equal to the first character of the next word.
# The last character of the last word is equal to the first character of the first word.
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s=sentence.split()
        if sentence[0]==sentence[-1]:
            for i in range(len(s)-1):
                if s[i][-1]!=s[i+1][0]:
                    return False
            return True
        else:
            return False
