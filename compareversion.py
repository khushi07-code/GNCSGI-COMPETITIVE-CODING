class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        answer=0
        num1=version1.split(".")
        num2=version2.split(".")              
        for i in range(max(len(num1),len(num2))):
            a=num1[i] if(i<len(num1)) else 0
            b=num2[i] if(i<len(num2)) else 0
            if int(a)<int(b):
                return -1
            elif int(a)>int(b):
                return  1

            
        return answer   
