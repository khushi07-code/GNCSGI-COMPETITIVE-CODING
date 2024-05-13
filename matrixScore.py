class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def change(j):
            for i in range(len(j)):
                if(j[i]==0):
                    j[i]=1
                else:
                    j[i]=0
            return j
        answer=0
        for i in grid:
            if(i[0]==0):
                i=change(i)
        for i in range(len(grid[0])):
            zero=0
            one=0
            for j in range(len(grid)):
                if(grid[j][i]==0):
                    zero+=1
                else:
                    one+=1
            if zero>one:
                for j in range(len(grid)):
                    grid[j][i]=0 if grid[j][i]==1 else 1
        for i in grid:
            b= int("".join(str(x) for x in i), 2)
            answer+=(b)
        return answer

        
