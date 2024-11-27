# Input: n = 5, queries = [[2,4],[0,2],[0,4]]

# Output: [3,2,1]

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def dijkstra(a):
            cost=[float('inf')]*n
            cost[0]=0
            for i in range(n-1):
                cost[i+1]=min(cost[i+1],cost[i]+1)
                for j in a:
                    if j[0]==i:
                        cost[j[1]]=min(cost[j[1]],cost[j[0]]+1)
                i+=1
            return cost[-1]
        answer=[]
        for i in range(1,len(queries)+1):
            answer.append(dijkstra(queries[:i]))
        return answer
