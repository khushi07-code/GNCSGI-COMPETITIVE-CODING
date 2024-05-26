
class Solution:
    def checkRecord(self, n: int) -> int:
        def count_LL(h):
            count=0
            for i in h:
                if(i=='L'):
                    count+=0
                    if count>2:
                        return False
            return True
        count=0
        comb=product(['A','P','L'],repeat=n)
        for i in comb:
            if i.count("A")<2 and count_LL(i):
                    count+=1
        m = 1000000007
        return count%m
