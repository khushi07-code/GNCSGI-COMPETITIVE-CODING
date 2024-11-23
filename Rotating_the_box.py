# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity



class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n=len(box)
        answer = [[0] * n for _ in range(len(box[0]))]
        for u in range(n):
            i=box[u]
            for j in range(len(i)):
                if i[j]=='.':
                    w=j-1
                    while (i[w]=='#'or i[w]=='.') and w>=0:
                        t=i[w+1]
                        i[w+1]=i[w]
                        i[w]=t
                        w=w-1 
            box[u]=i
        for i in range(n): 
            for j in range(len(box[0])): 
                answer[j][n - 1 - i] = box[i][j]
        return answer
            
