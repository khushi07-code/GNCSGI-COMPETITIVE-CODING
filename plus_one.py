# Increment the large integer by one and return the resulting array of digits.ex=>>[1,2,3]->[1,2,4] (123+1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        else :
            digits.reverse()
            carry=0
            for i in range(len(digits)):
                if i==0:
                    digits[i]=0
                    carry=1
                else:
                    if digits[i]<9:
                        digits[i]=digits[i]+1
                        digits.reverse()
                        return digits
                    else:
                        digits[i]=0
                        carry=1
            if carry==1:
                digits.append(1)
            digits.reverse()
            return digits
