#question: https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)}

        visited = set()

        max_area = float('-inf')

        def dfs(i, j):

            visited.add((i, j))

            if i == m or i < 0 or j == n or j < 0:

                return(0)

            if not grid[i][j]:

                return(0)

            else:

                area = 1

                for dx, dy in dirs:

                    if (i + dx, j + dy) not in visited:

                        area += dfs(i + dx, j + dy)

                return(area)

        for i in range(m):
            for j in range(n):

                if grid[i][j] and (i, j) not in visited:

                    max_area = max(max_area, dfs(i, j))

        return(max(0, max_area))

