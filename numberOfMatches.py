# Return the number of matches played in the tournament until a winner is decided.
class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams=n
        matches=0
        while teams>=2:
            if teams%2==0:  #teams is even
                matches+=(teams//2)
                teams=teams//2
            else: #teams is odd
                matches+=((teams-1)//2)
                teams=(teams-1)//2+1
        return matches
