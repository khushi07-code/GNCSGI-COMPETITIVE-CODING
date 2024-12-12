# Return the number of gifts remaining after k seconds.

import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            num=max(gifts)
            sq=int(math.sqrt(num))
            idx=gifts.index(num)
            gifts[idx]=sq
        return sum(gifts)
