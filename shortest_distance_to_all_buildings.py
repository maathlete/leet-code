#question: https://leetcode.com/problems/shortest-distance-from-all-buildings/description/

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        neighbors = {(-1, 0), (0, 1), (1, 0), (0, -1)}

        m, n = len(grid), len(grid[0])

        distance = [[0] * n for _ in range(m)]
        reach_count = [[0] * n for _ in range(m)]

        def bfs(source):

            seen_buildings = 1

            queue = [(source, 1)] 

            visited = set([source])

            while queue:

                node, steps = queue.pop(0)

                x, y = node[0], node[1]

                for dx, dy in neighbors:

                    if (0 <= x + dx < m) and (0 <= y + dy < n) and ((x + dx, y + dy) not in visited):

                        visited.add((x + dx, y + dy))

                        if grid[x+dx][y+dy] == 0:
                            
                            distance[x + dx][y + dy] += steps

                            reach_count[x + dx][y + dy] += 1

                            queue.append(((x + dx, y + dy), steps + 1))

                        elif grid[x + dx][y + dy] == 1:

                            seen_buildings += 1

                    else:

                        continue

            return(seen_buildings)

            
        total_houses = 0

        for i in range(m):

            for j in range(n):

                if grid[i][j] == 1:

                    total_houses += 1

        min_distance = float('inf')

        for i in range(m):

            for j in range(n):

                if grid[i][j] == 1:

                    if bfs((i, j)) != total_houses:

                        return(-1)

        for i in range(m):

            for j in range(n):

                if reach_count[i][j] == total_houses:
                    
                    min_distance = min(min_distance, distance[i][j])

        return(min_distance if min_distance < float('inf') else -1)
