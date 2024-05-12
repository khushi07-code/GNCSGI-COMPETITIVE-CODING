class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        temp=[[],[],[]]
        answer=[]*(len(grid)-2)
        for j in range(len(grid)-2):
            a=[]
            for i in range(len(grid)-2):
                temp[0]=grid[j][i:i+3]
                temp[1]=grid[j+1][i:i+3]
                temp[2]=grid[j+2][i:i+3]
                max_n=0
                for i in temp:
                    if max_n<max(i):
                        max_n=max(i)
                a.append(max_n)
            answer.append(a)   
        return answer
