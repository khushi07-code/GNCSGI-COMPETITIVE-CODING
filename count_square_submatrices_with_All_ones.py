class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
            rows = len(matrix)
            cols = len(matrix[0])
            count=0
            def ContinSubSeq(lst):
                size=len(lst)
                for start in range(size):
                    for end in range(start+1,size+1):
                        yield (start,end)
            for start_row,end_row in ContinSubSeq(list(range(rows))):
                for start_col,end_col in ContinSubSeq(list(range(cols))):
                    j=[i[start_col:end_col] for i in matrix[start_row:end_row] ]
                    if len(j)==len(j[0]):
                        f=1
                        for k in j:
                            if 0 in k:
                                f=0
                        if f==1:
                            count+=1
            return count
