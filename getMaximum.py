class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def goldsum(i,j,visited):
            if  0 <= i < len(grid) and 0 <= j < len(grid[0]) and  grid[i][j]!=0 and (i,j)not in visited:
                visited.append((i,j))
                mat=grid[i][j]+max(goldsum(i+1,j,visited),goldsum(i-1,j,visited),goldsum(i,j+1,visited),goldsum(i,j-1,visited))
                visited.remove((i,j))
                return mat
            return 0
        sum=0
        visited=[]
        for i in range(len(grid)):
              for j in range(len(grid[0])):
                sum=max(sum,goldsum(i,j,visited))
        return sum
        
