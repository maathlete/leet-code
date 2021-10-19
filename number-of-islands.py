class Solution:
    
    def dfs(self, r, c, visited, grid):
        
        if (r < 0 or  c < 0 or \
            r == self.ROWS or c == self.COLS or 
            (r,c) in visited or grid[r][c] == "0"):
            
            return
                    
        visited.add((r, c))

        self.dfs(r+1, c, visited, grid)
        self.dfs(r-1, c, visited, grid)
        self.dfs(r, c+1, visited, grid)
        self.dfs(r, c-1, visited, grid)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        count = 0

        visited = set()
        
        for r in range(self.ROWS):
            for c in range(self.COLS):
                
                if grid[r][c] == "0":
                    continue
                
                elif grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    self.dfs(r, c, visited, grid)
                
        return(count)
