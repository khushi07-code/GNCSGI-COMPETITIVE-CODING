# Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
# Output: [[11,9],[9,4],[4,5],[5,1]]

class Solution:
  def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
    ans = []
    graph = collections.defaultdict(list)
    outDegree = collections.Counter()
    inDegrees = collections.Counter()
    for start, end in pairs:
      graph[start].append(end)
      outDegree[start] += 1
      inDegrees[end] += 1
    def getStartNode() -> int:
      for u in graph.keys():
        if outDegree[u] - inDegrees[u] == 1:
          return u
      return pairs[0][0]  # Arbitrarily choose a node.

    def euler(u: int) -> None:
      stack = graph[u]
      while stack:
        v = stack.pop()
        euler(v)
        ans.append([u, v])


    euler(getStartNode())
    return ans[::-1]


        
