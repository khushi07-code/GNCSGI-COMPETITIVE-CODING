# You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

# A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

# Team a will be the champion of the tournament if there is no team b that is stronger than team a.

# Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        count=0
        a=0
        for i in range(n):
            if all(i!=v[1] for v in edges):
                a=i
                count+=1
        return a if count==1 else -1
