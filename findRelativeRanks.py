class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]: 
        temp=score.copy()
        answer=[""]*len(score)
        temp.sort(reverse=True)
        for i ,a in enumerate(temp):
            if(i==0):
                answer[score.index(a)]="Gold Medal"
            elif(i==1):
                answer[score.index(a)]="Silver Medal"
            elif(i==2):
                answer[score.index(a)]="Bronze Medal"
            else:
                answer[score.index(a)]=str(i+1)
        
        return answer
