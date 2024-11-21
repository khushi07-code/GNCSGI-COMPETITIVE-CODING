# You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

# A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

# Return the number of unoccupied cells that are not guarded.
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, j in guards:
            grid[i][j] = 1
        for i, j in walls:
            grid[i][j] = 2
        for i, j in guards:
            for y in range(j - 1, -1, -1):
                if grid[i][y] == 2 or grid[i][y] == 1:
                    break
                grid[i][y] = 3
            for y in range(j + 1, n):
                if grid[i][y] == 2 or grid[i][y] == 1:
                    break
                grid[i][y] = 3
            for x in range(i - 1, -1, -1):
                if grid[x][j] == 2 or grid[x][j] == 1:
                    break
                grid[x][j] = 3
            for x in range(i + 1, m):
                if grid[x][j] == 2 or grid[x][j] == 1:
                    break
                grid[x][j] = 3
        unguarded_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unguarded_count += 1
        
        return unguarded_count

